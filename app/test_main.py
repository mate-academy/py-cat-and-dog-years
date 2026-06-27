from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age: int, dog_age: int, expected: int",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (0, -1, [0, 0])])
def test_zero_equals_zero(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
