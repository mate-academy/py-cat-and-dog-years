from typing import Any

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ]
)
def test_different_values(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
    ]
)
def test_incorrect_values(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("100", "five"),
        ([1, 2, 3], None),
    ]
)
def test_incorrect_data_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
