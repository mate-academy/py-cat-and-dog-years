import pytest
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
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (16, 16, [1, 1]),
        (25, 30, [2, 3]),
        (-1, -1, [0, 0]),
        (1000, 1000, [246, 197]),
        (30, 30, [3, 3]),
        (50, 50, [8, 7]),
        (999, 999, [245, 197]),
        (9999, 9999, [2495, 1997])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list[int])\
        -> None:
    assert get_human_age(cat_age, dog_age) == expected
