from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,converted_ages_list",
    [
        pytest.param(
            -10, -1, [0, 0],
            id="should convert to 0 when age negative"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should convert to 0 when age equals 0"
        ),
        pytest.param(
            14, 13, [0, 0],
            id="should convert to 0 when age < 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id=(
                "should convert to zero "
                "when age is equal first 15 years"
            )
        ),
        pytest.param(
            23, 23, [1, 1],
            id=(
                "should convert to 1 when age between "
                "first 15 years and summa of first 15 years + next 9"
            )
        ),
        pytest.param(
            24, 24, [2, 2],
            id=(
                "should convert to 2 "
                "after the first 15 years "
                "and the following 9 have been already lived"
            )
        ),
        pytest.param(
            27, 27, [2, 2],
            id=(
                "should convert to 2 "
                "after the first 15 years "
                "and more than the following 9 have been already lived"
            )
        ),
        pytest.param(
            28, 28, [3, 2],
            id=(
                    "should convert to [3, 2] "
                    "after the first 15 years "
                    "and more than the following 9 have been already lived"
            )
        ),
        pytest.param(
            100, 100, [21, 17],
            id=(
                "should correctly add "
                "extra years for each age"
            )
        )
    ]
)
def test_check_first_and_next_years(
        cat_age: int,
        dog_age: int,
        converted_ages_list: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == converted_ages_list

@pytest.mark.parametrize(
    "cat_invalid_age,dog_invalid_age,error",
    [
        pytest.param(
            [], 24, TypeError,
            id="should raise error when not int"
        ),
        pytest.param(
            14, "22", TypeError,
            id="should raise error when not int"
        ),
        pytest.param(
            "two", (12, 1), TypeError,
            id="should raise error when not int"
        )
    ]
)
def test_invalid_datatypes(
        cat_invalid_age: Any,
        dog_invalid_age: Any,
        error: type[TypeError]
) -> None:
   with pytest.raises(error):
       get_human_age(cat_invalid_age, dog_invalid_age)

