import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [1, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
    ]
)
def test_get_human_age_normal(
        cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (50, 60, [8, 9]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_large(
        cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 5, [0, 0]),
        (5, -1, [0, 0]),
        (-3, -7, [0, 0]),
    ]
)
def test_get_human_age_negative(
        cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (10.5, 10, [0, 1]),
        ("15", 15, [0, 1]),
        (None, 10, [0, 1]),
        ([10], 10, [0, 1]),
    ]
)
def test_get_human_age_invalid_types(
        cat_age: Any, dog_age: Any, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
