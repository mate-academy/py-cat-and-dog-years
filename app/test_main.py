import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (10, 10, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
])
def test_get_human_age_for_small_equal_values(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (50, 50, [8, 7]),
    (60, 60, [11, 9]),
    (70, 70, [13, 11]),
    (80, 80, [16, 13]),
    (90, 90, [18, 15]),
    (100, 100, [21, 17]),
])
def test_get_human_age_for_large_equal_values(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (28, 28, [3, 2]),
    (27, 29, [2, 3]),
    (32, 31, [4, 3]),
    (30, 35, [3, 4]),
    (40, 41, [6, 5]),
    (39, 45, [5, 6]),
])
def test_get_human_age_for_different_values(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (50, 20, [8, 1]),
    (30, 100, [3, 17]),
    (100, 30, [21, 3]),
])
def test_get_human_age_for_mixed_values(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 15, [0, 1]),
    (15, 0, [1, 0]),
    (0, 24, [0, 2]),
    (24, 0, [2, 0]),
])
def test_get_human_age_for_zero_cases(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
