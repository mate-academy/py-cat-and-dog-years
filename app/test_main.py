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
        (28, 14, [3, 0]),
        (14, 28, [0, 2]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, f"Expected {expected}, but got {result}"
