from typing import Any
from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (3, 3, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (88, 88, [18, 14]),
    ]
)
def test_can_get_human_age(cat_age: int, dog_age: int,
                           result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Age: cat_to_human dog_to_human of {cat_age} and {dog_age} "
        f"should be equal to {result}")


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        ("1", 1, TypeError),
        (3, "3", TypeError),
        ([3], 3, TypeError),
        (3, {3}, TypeError),
        ((3, 3), None, TypeError),
        (None, None, TypeError),
    ]
)
def test_can_get_human_age_invalid_type(
        cat_age: Any,
        dog_age: Any,
        result: Any) -> None:
    with pytest.raises(result):
        get_human_age(cat_age, dog_age)
