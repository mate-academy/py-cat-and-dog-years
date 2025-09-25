import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
)
def test_ages(cat_age, dog_age, expected):
    """
    Test get_human_age for various cat/dog ages without using pytest.main.
    """
    assert get_human_age(cat_age, dog_age) == expected
