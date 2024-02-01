import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age", [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17]),
        pytest.param(-1, 100, [0, 17]),
    ],
    ids=[
        "should return zeros when value are zero",
        "should return zero if the value is less than zero human years",
        "first year of life",
        "same age but different for animals",
        "correct age converter in long term",
        "negative value for age",
    ]
)
def test_check_for_cat_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(5, [5], TypeError)
    ],
    ids=[
        "TypeError: list instead of int"
    ]
)
def test_invalid_input(
        cat_age: Any,
        dog_age: Any,
        expected: Any
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
