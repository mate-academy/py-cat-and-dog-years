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
        (1000000, 1000000, [249996, 199997]),
        (32, 0, [4, 0]),
        (0, 34, [0, 4]),
        (24, 29, [2, 3]),

        # Negative numbers
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-1, -1, [0, 0]),
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
        ("15", 15),
        (15, "15"),
    ],
)
def test_get_human_age_invalid_types(
    cat_age: str | int,
    dog_age: str | int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
