import pytest
from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-100, -100, [0, 0]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        ("cat", "dog"),
        (1.5, 15),
        (15, 1.5),
        (None, 15),
        (15, None),
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises((TypeError, ValueError)):
        main.get_human_age(cat_age, dog_age)
