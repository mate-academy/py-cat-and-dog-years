import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "age_cat, age_dog, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (10 ** 9, 10 ** 9, [249999996, 199999997]),
    ]
)
def test_get_human_age(age_cat: int, age_dog: int, expected: list) -> None:
    assert get_human_age(age_cat, age_dog) == expected


@pytest.mark.parametrize(
    "invalid_cat_age, invalid_dog_age",
    [
        ("3", 3),
        (3, "3"),
        (3.5, 3),
        (3, 3.5),
        (None, 3),
        (3, None),
        (True, 3),
        (3, False),
        ([3], 3),
    ]
)
def test_get_human_age_invalid_type_raises_type_error(
        invalid_cat_age: Any , invalid_dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_cat_age, invalid_dog_age)


@pytest.mark.parametrize(
    "negative_cat_age, negative_dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-100, -100),
    ]
)
def test_get_human_age_negative_raises_value_error(
        negative_cat_age: int, negative_dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(negative_cat_age, negative_dog_age)
