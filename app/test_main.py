
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 2]),
        (32, 32, [4, 3]),
        (33, 33, [4, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
        (28, 15, [3, 1]),
        (15, 28, [1, 2]),
        (32, 29, [4, 3]),
        (0, 100, [0, 17]),
        (100, 0, [21, 0]),
    ],
)
def test_age_boundaries(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-10, 15, [0, 1]),
        (15, -10, [1, 0]),
    ],
)
def test_negative_ages(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("hello", 15),
        (15, "hello"),
        (None, 15),
        (15, None),
    ],
)
def test_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
