import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="test cat and dog age below first year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test cat and dog age equal to first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test cat and dog second year"
            ),
            pytest.param(
                32,
                32,
                [4, 3],
                id="test cat and dog extra years"
            )
        ]
    )
    def test_should_return_correct_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
