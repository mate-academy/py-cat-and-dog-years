import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "should return 0 when cat and dog age is 0",
        "should return 0 when cat and dog age less then 15",
        "first 15 cat and dog years give 1 human age",
        "should return 1 cat years and 1 dog years",
        "24 cat and dog years should equal 2 human years",
        "should return 2 cat years and 2 dog years",
        "should return 3 cat years and 3 dog years",
        "should return 21 cat years and 17 dog years",
    ]
)
def test_human_age(cat_age: int,
                   dog_age: int,
                   expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
