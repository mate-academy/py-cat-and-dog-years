import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_years, human_years",
    [
        ([0, 0], [0, 0]),
        ([14, 14], [0, 0]),
        ([15, 15], [1, 1]),
        ([23, 23], [1, 1]),
        ([24, 24], [2, 2]),
        ([27, 28], [2, 2]),
        ([28, 29], [3, 3]),
        ([100, 100], [21, 17])
    ],
    ids=[
        "below_one_year_returns_zero",
        "below_one_year_returns_zero",
        "one_year_range_returns_one",
        "one_year_range_returns_one",
        "two_years_range_returns_two",
        "two_years_range_returns_two",
        "correctly_counts_consecutive_years",
        "correctly_counts_consecutive_years"
    ]
)
def test_animal_years_are_counted_correctly(
        animal_years: list,
        human_years: list
) -> None:
    assert get_human_age(*animal_years) == human_years
