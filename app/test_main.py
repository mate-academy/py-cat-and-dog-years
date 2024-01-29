from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_years_to_convert, dog_years_to_convert, expected_years",
    [
        (0, 0, [0, 0]),
        (24, 24, [2, 2]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1])
    ],
    ids=[
        "should return [0, 0] if both years are 0",
        "should return [2, 2] for cat and dog both 24 years",
        "should return [1, 1] for cat and dog both 15 years",
        "should return [1, 1] for cat and dog both 23 years"
    ]
)
def test_of_converting_animals_years_to_people_years(
        cat_years_to_convert: int,
        dog_years_to_convert: int,
        expected_years: tuple
) -> None:
    assert get_human_age(
        cat_years_to_convert,
        dog_years_to_convert
    ) == expected_years
