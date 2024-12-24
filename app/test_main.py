import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
])
def test_returns_zero_for_ages_below_first_year(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
])
def test_returns_one_for_ages_in_second_year_range(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
])
def test_returns_two_for_ages_in_third_year_range(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_returns_correct_age_for_years_after_second_year(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
