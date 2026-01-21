import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "in_cat_age,in_dog_age,expected_result",
        [
            pytest.param(
                15,
                15,
                [1, 1],
                id="test age 1st year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test age rounds below 2nd year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test age 2nd year"
            ),
            pytest.param(
                36,
                39,
                [5, 5],
                id="test 2 plus years"
            )
        ]
    )
    def test_function(self,
                      in_cat_age: int,
                      in_dog_age: int,
                      expected_result: list) -> None:
        assert get_human_age(in_cat_age, in_dog_age) == expected_result
