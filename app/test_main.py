from typing import List
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [15, 15]),
        (2, 2, [24, 24]),
        (3, 3, [28, 29]),
        (4, 4, [32, 34]),
        (5, 5, [36, 39]),
        (10, 10, [56, 64]),
        (15, 15, [76, 89]),
        (20, 20, [96, 114]),
        (100, 100, [416, 514]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: List[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected
