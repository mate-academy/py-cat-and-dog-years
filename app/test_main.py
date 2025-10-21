import pytest
from app.main import get_human_age

cases_zero = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
]

cases_one = [
    (15, 15, [1, 1]),
    (20, 20, [1, 1]),
    (23, 23, [1, 1]),
]

cases_two = [
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (27, 27, [2, 2]),
]

cases_after_second = [
    (28, 28, [3, 2]),
    (32, 32, [4, 3]),
    (40, 40, [6, 5]),
]

cases_large = [
    (100, 100, [21, 17]),
]


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_zero)
def test_should_return_zero_years_when_younger_than_first_stage(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_one)
def test_should_return_one_year_when_exactly_first_stage(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_two)
def test_should_return_two_years_when_exactly_second_stage(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_after_second)
def test_should_convert_correctly_after_second_stage(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_large)
def test_should_handle_large_ages_correctly(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
