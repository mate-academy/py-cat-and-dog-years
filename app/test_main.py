import pytest
from typing import Type

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_list",
        [
            (
                pytest.param(
                    0,
                    0,
                    [0, 0],
                    id="should work with zeroes values"
                )
            ),
            (
                pytest.param(
                    100,
                    100,
                    [21, 17],
                    id="should work with great values"
                )
            ),
            (
                pytest.param(
                    -15,
                    -15,
                    [0, 0],
                    id="should work with negative values"
                )
            ),
            (
                pytest.param(
                    14,
                    14,
                    [0, 0],
                    id="should work with boundary "
                       "condition values to zero human year"
                )
            ),
            (
                pytest.param(
                    23,
                    23,
                    [1, 1],
                    id="should work with boundary "
                       "condition values to one human year"
                )
            ),
            (
                pytest.param(
                    28,
                    28,
                    [3, 2],
                    id="should work with boundary "
                       "condition values to difference "
                       "in cet/dog human years"
                )
            )
        ]
    )
    def test_age_in_human_years(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_list: list
    ) -> None:
        assert get_human_age(
            initial_cat_age,
            initial_dog_age) == expected_list

    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_error",
        [
            (
                pytest.param(
                    "16",
                    "17",
                    TypeError,
                    id="Should raise error if "
                       "value for `cat_age` or `dog_age` is string"
                )
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age,
                          initial_dog_age)
