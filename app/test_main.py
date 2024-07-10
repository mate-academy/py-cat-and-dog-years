import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0, 0,
                [0, 0],
                id="test under 15 years #1"
            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="test under 15 years #2"
            ),
            pytest.param(
                15, 15,
                [1, 1],
                id="test 15 years"
            ),
            pytest.param(
                23, 23,
                [1, 1],
                id="test 23 years"
            ),
            pytest.param(
                24, 24,
                [2, 2],
                id="test 24 years"
            ),
            pytest.param(
                27, 27,
                [2, 2],
                id="test 27 years"
            ),
            pytest.param(
                28, 28,
                [3, 2],
                id="test 28 years"
            ),
            pytest.param(
                100, 100,
                [21, 17],
                id="test 100 years"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
