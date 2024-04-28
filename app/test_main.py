import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (-1, -11, [0, 0]),
        (400, 700, [96, 137]),
    ],
    ids=[
        "If cat and dog age = 0 should return [0, 0]",
        "Should return [0, 0]",
        "Should return [1, 1]",
        "Should return [3, 2]",
        "If age is negative, should return [0, 0]",
        "If age is large, should return [96, 137]",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("1", 1),
        (2, [2]),
        ({1: 2}, 3),
        (2, (1, 4)),

    ]
)
def test_rising_error_correctly(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age), (
            "Should return TypeError, if function receives not integer"
        )
