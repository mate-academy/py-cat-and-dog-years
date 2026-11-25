import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (35, 38, [4, 4]),
        (36, 39, [5, 5]),
        (15, 24, [1, 2]),
        (24, 15, [2, 1]),
        (100, 0, [21, 0]),
        (0, 100, [0, 17]),
        (100, 100, [21, 17]),
        (1000000, 1000000, [249996, 199997]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-100, 24),
        (24, -100),
    ],
)
def test_get_human_age_negative_values(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        ([], 15),
        (15, []),
        ({}, 15),
        (15, {}),
    ],
)
def test_get_human_age_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
