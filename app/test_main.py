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
    (100, 100, [21, 17]),
    (15, 0, [1, 0]),
    (16, 0, [1, 0]),
    (24, 0, [2, 0]),
    (25, 0, [2, 0]),
    (28, 0, [3, 0]),
    (29, 0, [3, 0]),
    (32, 0, [4, 0]),
    (33, 0, [4, 0]),
    (0, 15, [0, 1]),
    (0, 16, [0, 1]),
    (0, 24, [0, 2]),
    (0, 25, [0, 2]),
    (0, 29, [0, 3]),
    (0, 30, [0, 3]),
    (0, 34, [0, 4]),
    (0, 35, [0, 4]),
    (16, 30, [1, 3])
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-5, -10)
])
def test_negative_age_should_raise_value_error(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", "16"),
    (None, None),
    (115.6, -15.3),
    (16.5, 17.9),
    (15, "16"),
    (None, 13)
])
def test_should_raise_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
