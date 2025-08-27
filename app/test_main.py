import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (31, 31, [3, 3]),
            (32, 32, [4, 3]),
            (33, 33, [4, 3]),
            (34, 34, [4, 4]),
            (35, 38, [4, 4]),
            (36, 39, [5, 5]),
            (39, 43, [5, 5]),
            (40, 44, [6, 6]),
            (16, 49, [1, 7]),
            (44, 24, [7, 2]),
            (416, 514, [100, 100])
        ]
)
def test_get_human_age_valid_int(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age", 
    [
        (-1, 5),
        (5, -1),
        (-8, -7),
        (6, -2),
        (-7, 14)
    ]
)
def test_get_human_age_negative_ValueError(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("4", 5),
        (1, 4.25),
        ("cat", "dog"),
        (10, "15"),
        (5.5, 13),
        (11.25, 3.75),
        (0, None),
        (False, 17),
        ([3, 6], 5),
        (6, {"dog": 8})
    ]
)
def test_get_human_age_TypeError(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
