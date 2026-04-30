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
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
    (15, 0, [1, 0]),
    (0, 15, [0, 1]),
    (27, 0, [2, 0]),
    (28, 0, [3, 0]),
    (0, 28, [0, 2]),
    (0, 29, [0, 3]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, -1),
    (-5, 10),
    (10, -5),
])
def test_negative_ages_raise_exception(cat_age: int, dog_age: int) -> None:
    with pytest.raises(Exception):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", 15),
    (15, "15"),
    (None, 15),
    (15, None),
])
def test_invalid_types_raise_exception(cat_age: int, dog_age: int) -> None:
    with pytest.raises(Exception):
        get_human_age(cat_age, dog_age)
