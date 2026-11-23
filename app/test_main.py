from typing import Any

import pytest

from app.main import get_human_age


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
        (28, 29, [3, 3]),
        (32, 32, [4, 3]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (100, 100, [21, 17]),
    ],
)
def test_should_convert_cat_and_dog_ages_to_human_years(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-100, -100, [0, 0]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
    ],
)
def test_should_return_zero_human_years_for_negative_ages(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        ([15], 15),
    ],
)
def test_should_raise_type_error_for_incorrect_types(
    cat_age: Any,
    dog_age: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
