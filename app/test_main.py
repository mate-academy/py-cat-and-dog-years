import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,converted_ages_list",
    [
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
