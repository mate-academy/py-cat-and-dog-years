from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "before_age, at_age, expected_before, expected_at, animal_type",
    [
        (14, 15, [0, 0], [1, 1], "both"),
        (23, 24, [1, 1], [2, 2], "both"),
        (27, 28, [2, 2], [3, 2], "cat"),
        (28, 29, [3, 2], [3, 3], "dog"),
    ],
)
def test_get_human_age_boundaries(
    before_age: int,
    at_age: int,
    expected_before: list,
    expected_at: list,
    animal_type: str,
) -> None:
    assert get_human_age(before_age, before_age) == expected_before
    assert get_human_age(at_age, at_age) == expected_at


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
    with pytest.raises(ValueError):
        get_human_age(invalid_cat, invalid_dog)


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
