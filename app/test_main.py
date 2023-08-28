import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
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
        "0 cat/dog years should be 0 human age",
        "under 15 cat/dog years should be 0 human age",
        "15 cat/dog years give 1 human year",
        "under 24 cat/dog years should be 1 human age",
        "24 cat/dog years give 2 human year",
        "under 28 cat year and under 29 dog year should be 2 human age",
        "28 cat years and 28 dog year give 3/2 human years",
        "100 cat/dog years give 21/17 human years"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error", [
        ("12", 1, TypeError),
        ([], 1, TypeError),
        ({}, 1, TypeError),
        ((), 1, TypeError)
    ],
    ids=[
        "str value instead of int",
        "list value instead of int",
        "dict value instead of int",
        "tuple value instead of int",
    ]
)
def test_incorrect_value(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
