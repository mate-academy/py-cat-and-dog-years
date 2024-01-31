import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "If Cat and dog age is negative - should return [0, 0]",
        "Cat and dog age is 0 - should return [0, 0]",
        "Cat and dog age is 14, dog age is 14 - should return [0, 0]",
        "Cat and dog age is 15 - should return [1, 1]",
        "Cat and dog age is 23 - should return [1, 1]",
        "Cat and dog age is 24 - should return [2, 2]",
        "Cat and dog age is 27 - should return [2, 2]",
        "Cat and dog age is 28 - should return [3, 2]",
        "Cat and dog age is 100 - should return [21, 17]"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
