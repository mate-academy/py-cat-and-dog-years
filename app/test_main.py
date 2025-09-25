import pytest
from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year_boundary() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_human_year_boundary() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_third_human_year_boundary_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_various_ages(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected

