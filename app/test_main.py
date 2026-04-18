import pytest

from typing import Any
from app import main


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
        (28, 29, [3, 3]),
        (100, 0, [21, 0]),
        (0, 100, [0, 17]),
        (100, 100, [21, 17]),

        (-1, 10, [0, 0]),
        (10, -1, [0, 0]),
        (-100, -100, [0, 0]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_cat, invalid_dog",
    [
        ("5", 5),
        (5, "5"),
        (None, 5),
        (5, None),
        ([], 5),
        (5, []),
    ]
)
def test_get_human_age_raises_type_error_for_invalid_types(
        invalid_cat: Any, invalid_dog: Any
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(invalid_cat, invalid_dog)
