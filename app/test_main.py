from typing import List

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
    (100, 100, [21, 17]),
    (29, 28, [3, 2]),
    (50, 50, [8, 7]),
    (120, 120, [26, 21]),
    (100, 0, [21, 0]),
    (0, 100, [0, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, 10),
    (10, -1),
    (-5, -5),
    (10**6, 10**6),
])
def test_get_human_age_edge_cases(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(isinstance(age, int) and age >= 0 for age in result)


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", 15),
    (15, "15"),
    (None, 15),
    (15, None),
    ([15], 15),
    (15, [15]),
])
def test_get_human_age_invalid_data_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
