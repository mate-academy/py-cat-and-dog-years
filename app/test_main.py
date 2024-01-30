import pytest
from typing import Any, Type

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-5, -7, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "negative animal age should return zero",
        "zero animal age should return zero-s",
        "if animal age less than 15 should return 0",
        "if animal ages equal 15 should return [1, 1]",
        "if animal ages equal 23 should return [1, 1]",
        "if animal ages equal 24 should return [2, 2]",
        "if animal ages equal 28 should return [3, 2]",
        "if animal ages equal 100 should return [21, 17]",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("-5", -7, TypeError),
        (0, [0], TypeError),
    ],
    ids=[
        "Animal ages should be int, not str",
        "Animal ages should be int, not list",
    ]
)
def test_get_human_age_invalid(
        cat_age: Any,
        dog_age: Any,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
