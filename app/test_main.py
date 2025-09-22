
import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_years, dog_years, expected):
    assert get_human_age(cat_years, dog_years) == expected

@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        ("a", 10),
        (10, "b"),
        (None, 10),
        (10, None),
        (1.5, 10),
        (10, 2.7),
    ]
)
def test_invalid_types(cat_years, dog_years):
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_years, dog_years)
