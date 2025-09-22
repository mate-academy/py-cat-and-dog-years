from typing import Any

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        ("cat", 10, TypeError),
        (10.5, 10, TypeError),
        (-1, 10, ValueError),
    ]
)
def test_get_human_age_with_invalid_input(
        cat_age: Any,
        dog_age: Any,
        expected_exception: TypeError | ValueError
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
