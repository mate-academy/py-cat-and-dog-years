import pytest
from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
)
def test_get_human_age(cat_age: float, dog_age: float, expected: list[int]) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected
