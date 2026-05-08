import pytest
import app.main as main


DATA = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (15, 0, [1, 0]),
    (0, 15, [0, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (24, 23, [2, 1]),
    (23, 24, [1, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (99, 99, [20, 17]),
    (100, 100, [21, 17]),
    (-1, -1, [0, 0]),
    (-100, 10, [0, 0]),
    (10, -100, [0, 0]),
    (1000, 1000, [246, 197]),
    (1000000, 1000000, [249996, 199997]),
]


@pytest.mark.parametrize("cat_age,dog_age,expected", DATA)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected
