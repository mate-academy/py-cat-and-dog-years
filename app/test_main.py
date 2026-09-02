from typing import Any

import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (0, 15, [0, 1]),
    ],
    ids=[
        "zero_age",
        "below_first_threshold",
        "at_first_threshold",
        "below_second_threshold",
        "at_second_threshold",
        "before_third_increment",
        "cat_and_dog_diverge_after_second_threshold",
        "large_ages",
        "cat_zero_dog_above_threshold",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-1, -1),
    ],
    ids=["negative_cat_age", "negative_dog_age", "both_negative"],
)
def test_should_raise_value_error_for_negative_age(
    cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("5", 5),
        (5, "5"),
        (None, 5),
        (5, None),
        (5.5, 5),
        (5, 5.5),
    ],
    ids=[
        "cat_age_string",
        "dog_age_string",
        "cat_age_none",
        "dog_age_none",
        "cat_age_float",
        "dog_age_float",
    ],
)
def test_should_raise_type_error_for_invalid_type(
    cat_age: Any,
    dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
