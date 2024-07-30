import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_years, human_years",
    [
        ([0, 0], [0, 0]),
        ([14, 14], [0, 0])
    ]
)
def test_below_one_year_returns_zero(animal_years, human_years):
    assert get_human_age(*animal_years) == human_years

@pytest.mark.parametrize(
    "animal_years, human_years",
    [
        ([15, 15], [1, 1]),
        ([23, 23], [1, 1])
    ]
)
def test_one_year_range_returns_one(animal_years, human_years):
    assert get_human_age(*animal_years) == human_years


@pytest.mark.parametrize(
    "animal_years, human_years",
    [
        ([24, 24], [2, 2]),
        ([27, 28], [2, 2])
    ]
)
def test_two_years_range_returns_two(animal_years, human_years):
    assert get_human_age(*animal_years) == human_years


@pytest.mark.parametrize(
    "animal_years, human_years",
    [
        ([28, 29], [3, 3]),
        ([100, 100], [21, 17])
    ]
)
def test_correctly_counts_consecutive_years(animal_years, human_years):
    assert get_human_age(*animal_years) == human_years
