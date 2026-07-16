import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (30, 30, [3, 3]),
    (50, 50, [8, 7]),
    (100, 100, [21, 17])
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    (-1, 10),
    (10, -1),
    (-5, -5),
])
def test_get_human_age_invalid_inputs(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
