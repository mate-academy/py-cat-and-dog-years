
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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (24, 15, [2, 1]),
        (19, 19, [1, 1]),
        (-1, -1, [0, 0]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
        (1_000_000, 1_000_000, [249996, 199997]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
)
def test_invalid_types_raise_type_error(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
