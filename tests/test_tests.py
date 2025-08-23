import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [15, 15]),
        (2, 2, [24, 24]),
        (3, 3, [28, 29]),
        (4, 4, [32, 34]),
        (5, 5, [36, 39]),
    ]
)
def test_get_human_age(cat_years, dog_years, expected):
    assert get_human_age(cat_years, dog_years) == expected

def test_invalid_input():
    with pytest.raises(ValueError):
        get_human_age(-1, 3)
    with pytest.raises(ValueError):
        get_human_age(3, -1)
    with pytest.raises(ValueError):
        get_human_age("two", 3)
    with pytest.raises(ValueError):
        get_human_age(3, "three")