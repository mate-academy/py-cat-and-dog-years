import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        (
            0, 0, [0, 0]
        ),
        (
            14, 14, [0, 0]
        ),
        (
            15, 15, [1, 1]
        ),
        (
            23, 23, [1, 1]
        ),
        (
            24, 24, [2, 2]
        ),
        (
            27, 27, [2, 2]
        ),
        (
            28, 28, [3, 2]
        ),
        (
            100, 100, [21, 17]
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        (
            -1, 5, [0, 0]
        ),
        (
            5, -1, [0, 0]
        ),
        (
            -100, -100, [0, 0]
        ),
    ]
)
def test_get_human_age_negative_inputs(
        cat_age: int,
        dog_age: int,
        expected_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (
            "15", 15
        ),
        (
            15, "15"
        ),
        (
            None, 15
        ),
        (
            15, None
        ),
        (
            [15], 15
        ),
    ]
)
def test_get_human_age_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
