from app.main import get_human_age
from typing import Any
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_parametrized(cat_age: int, dog_age: int,
                                    expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,exc",
    [
        (-5, -10, ValueError),
        (14.5, "5", TypeError),
    ],
)
def test_get_human_age_errors(cat_age: Any, dog_age: Any, exc: [Exception]) -> None:
    with pytest.raises(exc):
        get_human_age(cat_age, dog_age)
