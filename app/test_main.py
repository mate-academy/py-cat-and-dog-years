import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        # Before and at first boundary
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        # Before and at second boundary
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # Cat: before and at next boundary
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        # Dog: before and at next boundary
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        # Next boundaries
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        # Large values
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-100, -100),
    ],
)
def test_get_human_age_with_negative_ages(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 1),
        (1, "1"),
        (1.5, 1),
        (1, 2.5),
        (None, 1),
        (1, None),
        ([], 1),
        (1, {}),
    ],
)
def test_get_human_age_with_invalid_types(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
