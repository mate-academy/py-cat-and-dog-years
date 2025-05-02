import pytest
from app.main import get_human_age
from typing import List, Any


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),

    (16, 16, [1, 1]),
    (30, 30, [3, 3]),
    (31, 31, [3, 3]),
    (32, 32, [4, 3]),
    (40, 40, [6, 5]),
    (50, 50, [8, 7]),
    (60, 60, [11, 9]),
    (70, 70, [13, 11]),
    (80, 80, [16, 13]),
    (90, 90, [18, 15]),
    (99, 99, [20, 17])
])
def test_get_human_age(
        cat_age: int, dog_age: int, expected: List | int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (-1, 10),
    (10, -1),
    (-5, -5),
])
def test_get_human_age_negative_ages(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
    assert all(x >= 0 for x in result)


@pytest.mark.parametrize("cat_age, dog_age", [
    ("15", 15),
    (15, "15"),
    ("fifteen", 15),
    (15, None),
    (None, 15),
    (15.5, 15),
    (15, 15.5),
    ([], 15),
    (15, {}),
])
def test_get_human_age_other_invalid_types(cat_age: Any, dog_age: Any) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
    except (TypeError, ValueError):
        pass
    else:
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(x, int) for x in result)
