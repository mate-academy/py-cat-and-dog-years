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
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ]
)
def test_get_human_age_negative_values(cat_age, dog_age):
    with pytest.raises(ValueError, match="must be non-negative"):
        get_human_age(cat_age, dog_age)

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (10, "15"),
        (None, 10),
        (10, None),
        ([15], 10),
        (10, {"age": 15}),
    ]
)
def test_get_human_age_invalid_types(cat_age, dog_age):
    with pytest.raises(TypeError, match="must be integers"):
        get_human_age(cat_age, dog_age)
