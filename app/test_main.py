from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, -100, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100.001, 100, [21, 17])
    ],
    ids=[
        "negative values should return 0 human age",
        "0 age should return 0 human age",
        "14 cat and dog ages should return 0 human age",
        "15 cat and dog ages should return 1 human age",
        "23 cat and dog ages should return 1 human age",
        "24 cat and dog ages should return 2 human age",
        "27 cat and dog ages should return 2 human age",
        "28 cat and dog ages should return 3 and 2 human age",
        "100 cat and dog ages should return 21 and 17 human age",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("1", "1", TypeError),
        ([1], [1], TypeError),
        (1j, 1j, TypeError),
        ({1}, {1}, TypeError),
    ],
    ids=[
        "'TypeError' should be raised when function receives a string",
        "'TypeError' should be raised when function receives a list",
        "'TypeError' should be raised when function receives a complex",
        "'TypeError' should be raised when function receives a set",
    ]
)
def test_should_raise_correct_error(
    cat_age: Any,
    dog_age: Any,
    expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
