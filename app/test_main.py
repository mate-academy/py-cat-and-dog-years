import pytest

from typing import Any
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
        (100, 100, [21, 17]),
        (15, 24, [1, 2]),
    ]
)
def test_get_human_age_valid_inputs(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -10),
        (-5, -5)
    ]
)
def test_get_human_age_raises_value_error_for_negative_ages(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "24"),
        (15.5, 15),
        (15, [10]),
        (True, 15),
    ]
)
def test_get_human_age_raises_type_error_for_invalid_types(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
