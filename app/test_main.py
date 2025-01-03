import pytest
from app.main import get_human_age


class Animal:
    @pytest.mark.parametrize(
        "cat_age",
        "dog_age",
        "result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should_zero_cat_and_dog"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should_one_year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should_one_years"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should_two_year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should_two_and_three_year"
            ),
        ]
    )

    def test_modify_class(self, cat_age: int,
                          dog_age: int,
                          result: list) -> None:
        cat = cat_age
        dog = dog_age
        get_human_age(cat, dog)
        assert get_human_age == result
