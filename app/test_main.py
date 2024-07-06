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
        (32, 32, [4, 3]),
        (33, 33, [4, 3]),
        (100, 100, [21, 17])
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> bool:
    assert get_human_age(cat_age, dog_age) == expected


def test_large_numbers() -> bool:
    assert get_human_age(1000, 1000) == [246, 197]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
)
def test_incorrect_types(cat_age: int, dog_age: int) -> bool:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15.5, 15),
        (15, 15.5),
    ],
)
def test_float_types(cat_age: float, dog_age: float) -> bool:
    result = get_human_age(cat_age, dog_age)
    if isinstance(cat_age, float):
        assert result[0] == get_human_age(int(cat_age), dog_age)[0]
    if isinstance(dog_age, float):
        assert result[1] == get_human_age(cat_age, int(dog_age))[1]
