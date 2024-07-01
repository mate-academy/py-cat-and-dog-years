from typing import Type

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        (-5, -1, [0, 0]),
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
        "negative animal age should convert to 0",
        "Should return [0, 0]",
        "if age is less 15",
        "if age is equal 15",
        "if age is equal 23",
        "if age is equal 24",
        "if age is equal 27",
        "If age is over 24",
        "Big numbers",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "initial_cat_age,initial_dog_age,expected_error",
    [
        ("something", "something", TypeError),
        (15, "something", TypeError),
        ("something", 15, TypeError),
    ]
)
def test_get_human_age_errors(
        initial_cat_age: int,
        initial_dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(initial_cat_age, initial_dog_age)
