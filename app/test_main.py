from typing import Any
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
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_cat, invalid_dog",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ],
)
def test_get_human_age_negative_ages(
    invalid_cat: int, invalid_dog: int
) -> None:
    assert get_human_age(invalid_cat, invalid_dog) == [0, 0]


@pytest.mark.parametrize(
    "wrong_cat, wrong_dog",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
    ],
)
def test_get_human_age_invalid_types(
    wrong_cat: Any, wrong_dog: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(wrong_cat, wrong_dog)
