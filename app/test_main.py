from app.main import get_human_age

import pytest
import app.main


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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 2000, [246, 397]),
        (14, 0, [0, 0]),
        (15, 0, [1, 0]),
        (23, 0, [1, 0]),
        (24, 0, [2, 0]),
        (27, 0, [2, 0]),
        (28, 0, [3, 0]),
        (32, 0, [4, 0]),
        (0, 14, [0, 0]),
        (0, 15, [0, 1]),
        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (0, 27, [0, 2]),
        (0, 28, [0, 2]),
        (0, 29, [0, 3]),
        (0, 34, [0, 4]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected
