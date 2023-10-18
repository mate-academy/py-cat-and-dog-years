import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Both are negative",
        "Both are 0",
        "Both are 14",
        "Cat: 15, Dog: 15",
        "Cat: 23, Dog: 23",
        "Cat: 24, Dog: 24",
        "Cat: 27, Dog: 27",
        "Cat: 28, Dog: 28",
        "Cat: 100, Dog: 100",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected, \
        f"Result should be equal to {expected}"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("cat_age", 10),
        (10, "dog_age"),
        ("cat_age", "dog_age"),
        ([10], 10),
        (10, [10]),
        ([10], [10]),
        ((10,), 10),
        (10, (10,)),
        ((10,), (10,)),
    ],
    ids=[
        "Both are strings",
        "Cat is string, Dog is int",
        "Both are strings",
        "Cat is list, Dog is int",
        "Cat is int, Dog is list",
        "Both are lists",
        "Cat is tuple, Dog is int",
        "Cat is int, Dog is tuple",
        "Both are tuples",
    ]
)
def test_get_human_age_with_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
