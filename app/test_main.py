import pytest
from typing import Any

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
        (100, 100, [21, 17])
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
        "100/100 cat/dog years should convert into 21/17 human age.",
    ]
)
def test_ages(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 1),
        (1, -1),
        (-1, -1),
    ],
    ids=[
        "negative_cat_age",
        "negative_dog_age",
        "both_negative"
    ],
)
def test_should_raise_value_error_for_negative_age(
    cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 1),
        (1, "1"),
        (None, 1),
        (1, None)
    ],
    ids=[
        "cat_age_string",
        "dog_age_string",
        "cat_age_none",
        "dog_age_none"
    ],
)
def test_should_raise_type_error_for_invalid_type(
    cat_age: Any,
    dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
