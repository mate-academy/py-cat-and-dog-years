from typing import Any

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-10, -20, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (31, 28, [3, 2]),
        (32, 29, [4, 3]),
        (28, 33, [3, 3]),
        (28, 34, [3, 4]),
        (100, 100, [21, 17]),
        (10000, 20000, [2496, 3997])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (82.91, 22.11, ValueError),
        ("15", "15", ValueError),
        (None, None, ValueError),
        (15, None, ValueError),
        (None, 15, ValueError),
        (15, "20", ValueError),
        ([15], 15, ValueError)
    ]
)
def test_get_human_age_invalid(
        cat_age: Any,
        dog_age: Any,
        expected: type[Exception]
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
