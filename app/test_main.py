from typing import List
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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_returns_correct_values(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 10, [0, 2]),
        (10, -5, [0, 0]),
        (-3, -7, [0, 0]),
    ],
)
def test_get_human_age_with_negative_values(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 14, [1, 0]),
        (23, 22, [1, 1]),
        (28, 27, [3, 2]),
    ],
)
def test_cat_and_dog_ages_change_independently(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
