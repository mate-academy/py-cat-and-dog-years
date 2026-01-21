import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (16, 16, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (31, 29, [3, 3]),
    (32, 34, [4, 4]),
    (35, 35, [4, 4]),
    (36, 39, [5, 5]),
    (100, 100, [21, 17]),
])
def test_human_age_values_and_types(cat_age: int, dog_age: int, expected: list[int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, 5),
    (5, -1),
    (-10, -20),
])
def test_negative_ages_raise_valueerror(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age", [
    (15.5, 20),
    ("15", 20),
    (15, None),
    (None, 15),
])
def test_invalid_type_raises_typeerror(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
