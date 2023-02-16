from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("15", 0, TypeError),
        (15, "15", TypeError)

    ]
)
def test_should_raise_type_error(
        cat_age: Any,
        dog_age: Any,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (0, 0, [0, 0]),
        (-15, -15, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (101, 101, [21, 17])
    ]
)
def test_should_return_correct_value_for_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(
        cat_age,
        dog_age
    ) == expected_human_age
