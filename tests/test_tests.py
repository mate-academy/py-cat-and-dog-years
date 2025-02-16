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
        (16, 16, [1, 1]),  # Just above 15
        (25, 25, [2, 2]),  # Just above 24
        (30, 30, [3, 3]),  # Just above 28
        (50, 50, [8, 7]),  # Midway case
        (200, 200, [46, 37]),  # Large numbers
    ],
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
