from typing import Any

import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (30, 30, [3, 3]),
    (31, 31, [3, 3]),
    (32, 32, [4, 3]),
    (34, 34, [4, 4]),
    (35, 35, [4, 4]),
    (36, 36, [5, 4]),
    (100, 100, [21, 17]),
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (-1, 10, [0, 0]),
    (10, -1, [0, 0]),
    (-5, -5, [0, 0]),
])
def test_get_human_age_negative_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    ("5", 10),
    (10, "5"),
    (None, 10),
    (10, None),
    ([15], 15),
    (15, {"age": 15}),
])
def test_get_human_age_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
