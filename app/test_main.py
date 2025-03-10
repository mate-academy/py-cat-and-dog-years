import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 14, [1, 0]),
        (24, 23, [2, 1]),
        (27, 29, [2, 3]),
        (30, 30, [3, 3]),
        (-1, 10, [0, 0]),
        (10, -1, [0, 0]),
        (-5, -5, [0, 0]),
        (0, 0, [0, 0]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
