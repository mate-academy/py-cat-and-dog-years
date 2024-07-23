from typing import Any

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (0, 30, [0, 3]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_converted_amount_of_years(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Convert to human age is incorrect"


def test_should_work_with_large_numbers() -> None:
    assert (
        get_human_age(4567890, 4567890) == [1141968, 913575]
    ), "Function should work with large numbers"


def test_should_return_zero_to_negative_numbers() -> None:
    assert (
        get_human_age(-1, -1) == [0, 0]
    ), "Function should return zero to negative numbers"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("a", 1),
        ("a", "b"),
        ([1, 2], {"a": 1}),
    ],
    ids=[
        "1 string types",
        "2 string types",
        "1 list, 1 dict type"

    ]
)
def test_with_incorrect_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age",
    [
        15,
        ()
    ],
    ids=["1 argument", "0 arguments"]
)
def test_with_not_enough_arguments(cat_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age)
