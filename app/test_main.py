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
def test_valid_inputs(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -8),
    ]
)
def test_negative_values(cat_age, dog_age):
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("abc", 10),
        (10, "xyz"),
        ("10", "5"),
        (None, 5),
        (5, None),
        (3.5, 10),
        (10, 2.8),
    ]
)
def test_incorrect_types(cat_age, dog_age):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
