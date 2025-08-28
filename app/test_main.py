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
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (28, 3),
    ],
)
def test_cat_boundaries(cat_age: int, expected: int) -> None:
    human_cat, _ = get_human_age(cat_age, 0)
    assert human_cat == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (29, 3),
        (34, 4),
    ],
)
def test_dog_boundaries(dog_age: int, expected: int) -> None:
    _, human_dog = get_human_age(0, dog_age)
    assert human_dog == expected
