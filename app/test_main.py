import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (32, 32, [4, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age_valid_cases(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", 15),
    (15, "15"),
    (15.5, 15),
    (None, 15),
])
def test_get_human_age_invalid_type_raises_error(cat_age, dog_age):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
