from app.main import get_human_age
import pytest
from typing import List


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
def test_get_human_age_basic(cat_age: int, dog_age: int, expected: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1, 1, [0, 0]),
        (15, 14, [1, 0]),
        (16, 15, [1, 1]),
        (33, 34, [3, 3]),
        (36, 40, [4, 4]),
    ]
)
def test_get_human_age_edge_cases(cat_age: int, dog_age: int, expected: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ]
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 10),
        (10, None),
        (5.5, 10),
        (10, 5.5),
    ]
)
def test_get_human_age_invalid_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
