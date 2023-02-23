import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 23, [1, 1]),
        (25, 25, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "-1, -1 should return [0, 0]",
        "0, 0, should return [0, 0]",
        "14, 14, should return [0, 0]",
        "15, 23, should return [1, 1]",
        "25, 25, should return [2, 2]",
        "28, 28, should return [3, 2]",
        "100, 100, should return [21, 17]"
    ]
)
def test_human_age(cat_age: int, dog_age: int, human_age:int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize("cat_age, dog_age, human_age", [
    ("one", 1, TypeError),
    (1, "one", TypeError),
    ("one", "one", TypeError),
])
def test_get_human_age_errors(
        cat_age: int,
        dog_age: int,
        human_age: Any
) -> None:
    with pytest.raises(human_age):
        get_human_age(cat_age, dog_age)
