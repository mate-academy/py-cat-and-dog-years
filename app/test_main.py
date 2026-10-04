import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (1_000_000, 1_000_000, [249_996, 199_997]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
    ],
)
def test_get_human_age_rejects_negative_ages(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        (1.5, 0),
        (0, 1.5),
        ("1", 0),
        (0, "1"),
        (True, 0),
        (0, False),
        (None, 0),
        (0, None),
    ],
)
def test_get_human_age_rejects_non_integer_ages(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
