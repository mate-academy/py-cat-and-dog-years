import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="test all zero param age"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="test all param below 1st human age"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="test 1st grade human age"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="test all param below 2nd human age"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="test 2nd human age"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="test all param below 3rd human age"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="test 3rd human age"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="test above 3rd human age"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
