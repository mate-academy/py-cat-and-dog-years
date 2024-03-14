from app.main import get_human_age
import pytest

# write your code here


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (1, 1, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (25, 25, [2, 2]),
        (32, 34, [4, 4]),
        (28, 39, [3, 5]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
