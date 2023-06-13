import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "negative cat/dog age should return 0",
        "zero cat/dog age should return 0",
        "less 15 years cat/dog should return 0",
        "15 cat/dog years should return 1",
        "cat/dog years in range 15-24 should return 1",
        "24 cat/dog years should return 2",
        "cat/dog years in range 24-27 should return 2",
        "28 cat/dog years should return [3, 2]",
        "29 dog years should return 3",
        "100 cat/dog years should return [21, 17]",
    ]
)
def test_converting_to_human_age_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ([1], 1, TypeError),
        (13, "13", TypeError),
    ],
    ids=[
        "should raise error when cat age isn't int",
        "should raise error when dog age isn't int",
    ]
)
def test_raising_error_correctly(
        cat_age: Any,
        dog_age: Any,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
