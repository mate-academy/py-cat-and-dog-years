import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
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
    ), "Incorrect conversion to human years"


def test_should_return_zero_to_negative_numbers() -> None:
    assert (
        get_human_age(-5, -12) == [0, 0]
    ), "the function should return zeros if the numbers are negative"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (150, 120, [33, 21]),
        (1234, 4321, [304, 861]),

    ]
)
def test_for_large_values(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Values that are too large"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("b", []),
        ("a", [1, ]),

    ]
)
def test_with_incorrect_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age), "Invalid data type"
