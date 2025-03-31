from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "first_year,second_year,converted_cat_year,converted_dog_year",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17),
        (100.1, 100, 21, 17),
        (100, 100.2, 21, 17),
        (100.7, 100, 21, 17),
        (100, 100.7, 21, 17),
    ],
)
def test_correct_ages_convert(
        first_year: int | float,
        second_year: int | float,
        converted_cat_year: int,
        converted_dog_year: int
) -> None:

    assert (get_human_age(first_year, second_year)
            == [converted_cat_year, converted_dog_year])
