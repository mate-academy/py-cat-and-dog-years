import pytest
from app import main


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age,dog_age", [
    (-1, 5),
    (5, -1),
    (-10, -10),
])
def test_get_human_age_negative(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    ("5", 5),
    (5, "5"),
    (5.0, 5),
    (None, 5),
])
def test_get_human_age_invalid_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
