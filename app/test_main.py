from app.main import get_human_age
from typing import Any
import pytest


@pytest.mark.parametrize("cat, dog, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),

])
def test_get_human_age(cat: int, dog: int, expected: list) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize("cat, dog", [
    (-1, 0),
    (0, -10),
    (-3, -5)
])
def test_negative_ages_raise_value_error(cat: int, dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)


@pytest.mark.parametrize("cat, dog", [
    ("1", 2),
    (1.5, 2),
    (None, 2),
    (2, "dog"),
])
def test_invalid_types_raise_type_error(cat: Any, dog: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
