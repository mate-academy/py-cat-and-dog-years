import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (36, 39, [5, 5]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat: int, dog: int, expected: list[int]) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "cat, dog",
    [
        (-1, 10),
        (10, -1),
        ("15", 10),
        (10, "15"),
        (15.5, 10),
        (10, 20.5),
        (None, 10),
        (10, None),
    ]
)
def test_invalid_input(cat: object, dog: object) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)
