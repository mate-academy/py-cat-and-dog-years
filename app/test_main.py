import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 14, [1, 0]),
        (14, 15, [0, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 23, [2, 1]),
        (23, 24, [1, 2]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 24, [3, 2]),
        (24, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_boundary_and_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_cat,invalid_dog",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 16),
        (15, 16.0),
        (None, 10),
        (10, None),
        (True, 10),
        (10, False),
    ],
)
def test_get_human_age_invalid_types_raise_error(
    invalid_cat: object,
    invalid_dog: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_cat, invalid_dog)  # type: ignore
