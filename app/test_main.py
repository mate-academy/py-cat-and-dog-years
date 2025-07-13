from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (-3, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_correct_list_of_human_ages(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("3", [1]),
        (None, None)
    ]
)
def test_get_human_age_should_take_only_int(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
