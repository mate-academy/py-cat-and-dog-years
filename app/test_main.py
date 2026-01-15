import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
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
def test_get_human_age_valid_inputs(cat_age: int,
                                    dog_age: int,
                                    expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("10", 10, TypeError),
        (10, "dog", TypeError),
        (-1, 10, ValueError),
        (10, -5, ValueError),
    ]
)
def test_get_human_age_raises_errors(cat_age: Any,
                                     dog_age: Any,
                                     expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
