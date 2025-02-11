import pytest
from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4])
    ])
def test_convert_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert (get_human_age(cat_age, dog_age) == expected)
