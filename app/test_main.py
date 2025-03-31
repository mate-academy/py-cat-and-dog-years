from typing import Any


import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (-1, -1, [0, 0]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Expected human age 0 for cat age 0 and dog age 0",
        "Expected human age 0 for cat age 14 and dog age 14",
        "Expected human age 1 for cat age 23 and dog age 23",
        "Expected human age 1 for cat age 23 and dog age 23",
        "Expected human age 2 for cat age 24 and dog age 24",
        "Expected human age 2 for cat age 27 and dog age 27",
        "Expected human age for cat:3 and dog:2 for cat age 28 and dog age 28",
        "Expected human age 0 for cat age -1 and dog age -1",
        "Expected human age for cat:21 and dog:17 for cat and dog ages 100",
    ],
)
def test_get_human_age_with_param_deco(
    cat_age: int, dog_age: int, expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ([], []),
        ((), ()),
        ("", ""),
        ({}, {})
    ],
    ids=[
        "TypeError raised when input is two lists",
        "TypeError raised when input is two tuples",
        "TypeError raised when input is two strings",
        "TypeError raised when input is two dicts",
    ],
)
def test_get_human_age_with_param_error(
    cat_age: Any,
    dog_age: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
