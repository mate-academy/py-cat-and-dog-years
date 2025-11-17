import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_years",
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
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_years: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_years


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -7),
    ]
)
def test_negative_values_raise(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("abc", 10),
        (10, "xyz"),
        (1.5, 10),
        (10, 2.7),
        (None, 10),
        ([], 10),
        (10, {}),
    ]
)
def test_wrong_type_raises(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
