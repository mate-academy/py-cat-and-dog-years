import pytest
from typing import Any
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
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (24, 0, [2, 0]),
        (0, 24, [0, 2]),
        (28, 0, [3, 0]),
        (0, 29, [0, 3]),
    ]
)
def test_get_human_age_valid(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, -1),
        (-10, 5),
        (5, -10),
    ]
)
def test_negative_values(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("abc", 10),
        (10, "xyz"),
        (3.14, 10),
        (10, 2.71),
        (None, 10),
        (10, None),
    ]
)
def test_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
