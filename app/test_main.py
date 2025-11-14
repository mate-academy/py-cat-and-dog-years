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
    ]
)
def test_get_human_age_common(cat_age: int,
                              dog_age: int, expected: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-5, -10),
    ]
)
def test_negative_ages(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (10, "20"),
        ("abc", "xyz"),
        (3.14, 2.71),
        (None, 0),
        (0, None),
    ]
)
def test_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
