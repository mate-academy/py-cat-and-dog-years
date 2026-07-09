from app.main import get_human_age
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ],
    ids=str
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "error_cat, error_dog",
    [
        ("cat", "dog"),
        ((1, 15), (1, 3)),
        ([2, "str"], [1, "str"]),
    ],
    ids=str
)
def test_should_raise_type_error_for_invalid_data_type(
        error_cat: Any,
        error_dog: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(error_cat, error_dog)
