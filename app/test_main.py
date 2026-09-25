from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (-10, -5, [0, 0]),
    ],
)
def test_get_human_age_conversions(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_cat_age,invalid_dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, [15]),
    ],
)
def test_get_human_age_invalid_types_raise_exception(
    invalid_cat_age: Any, invalid_dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_cat_age, invalid_dog_age)
