from typing import List, Any
import pytest
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
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, -10, [0, 0]),
        (-5, 10, [0, 0]),
        (10, -7, [0, 0]),
    ],
)
def test_get_human_age_negative_inputs(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    """
    For negative inputs the function should not produce negative results.
    With current rules, any age < 15 maps to 0 human years.
    """
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("a", "b"),
        (3.5, 10.2),
        (None, 5),
        ([1, 2], {"dog": 3}),
    ],
)
def test_get_human_age_invalid_types(cat_age: Any, dog_age: Any) -> None:
    """Function should raise TypeError for invalid input types."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
