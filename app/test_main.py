import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (-1, -1, [0, 0]),
        (-35, -45, [0, 0]),
        (-1, 18, [0, 1]),
        (14, 15, [0, 1]),
        (26, 12, [2, 0])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("cat", "dog"),
        ("11", "12"),
        ([3], [5]),
        ({3}, {0}),
        ((1, 2), (3)),
        ({"cat": 1}, {"dog": 2})
    ]
)
def test_invalid_values(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
