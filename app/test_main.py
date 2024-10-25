import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="return zeros if animal's years less than 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="return 1 human's year if animal's years equal to 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="return 1 human's year if animal's years less than 24"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="return 2 human's year's if animal's years equal to 24"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="convert cat's and dog's years into 3 human age"
        ),
        pytest.param(
            500, 500, [121, 97],
            id="convert animal's years into some human years"
        )

    ]
)
def test_pets_age(
        cat_years: int,
        dog_years: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result
