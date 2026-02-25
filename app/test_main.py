import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_examples_and_boundaries(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 0),
        (0, -1),
        (-5, -10),
    ],
)
def test_negative_ages_raise_value_error(cat_age, dog_age):
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("1", 0),
        (0, "1"),
        (1.5, 0),
        (0, 2.7),
        (None, 0),
        (0, None),
        ([], 0),
        (0, {}),
    ],
)
def test_invalid_types_raise_type_error(cat_age, dog_age):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)