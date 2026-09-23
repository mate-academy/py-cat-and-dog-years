import pytest

from app.main import get_human_age


def test_dog_extra_step() -> None:
    assert get_human_age(28, 29) == [3, 3]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (31, 32, [3, 3]),
        (32, 33, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_parametrized(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-5, 10, [0, 0]),
        (-1, -1, [0, 0]),
        (-100, -100, [0, 0]),
    ],
)
def test_negative_ages(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("cat", "dog"),
        ([15], {15}),
        (None, None),
    ],
)
def test_invalid_types_raise_type_error(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
