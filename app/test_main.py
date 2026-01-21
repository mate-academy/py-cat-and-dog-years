import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (32, 56, [4, 8]),
        (-2, 78, [0, 12]),
        (46, -7, [7, 0])
    ]
)
def test_should_return_correct_ages(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected_human_ages


@pytest.mark.parametrize(
    "cat_age, dog_age, exception_type",
    [
        ([], 12, TypeError),
        ("cat", 4, TypeError),
        (6, [], TypeError),
        (5, "dog", TypeError)
    ]
)
def test_should_raise_type_error(
        cat_age: Any,
        dog_age: Any,
        exception_type: Exception
) -> None:

    with pytest.raises(exception_type):
        get_human_age(cat_age, dog_age)
