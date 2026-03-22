from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        (-3, 3, ValueError),
        (3, -3, ValueError),
        ("6", 3, TypeError),
        (6, "3", TypeError),
    ]
)
def test_should_raise_error_for_invalid_input(
        cat_age: int | str,
        dog_age: int | str,
        expected_exception: Type[Exception],
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
