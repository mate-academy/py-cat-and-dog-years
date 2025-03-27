import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (25, 25, [2, 2]),
        (14, 14, [0, 0]),
        (9, 9, [0, 0]),
        (30, 35, [3, 4]),
        (100, 100, [21, 17]),
        (10, 50, [0, 7]),
        (100, 10, [21, 0])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
