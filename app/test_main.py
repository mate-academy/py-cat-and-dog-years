"""Tests for get_human_age:
- thresholds and typical cases
- large values
- negatives (treated as 0 human years)
- incorrect input types (TypeError)
"""

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (-1, 0, [0, 0]),
        (-10, 0, [0, 0]),
        (0, -1, [0, 0]),
        (0, -25, [0, 0]),
        (-3, -7, [0, 0]),
    ],
)
def test_negative_inputs_return_zero(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    """
    Negative ages are out of normal range. We treat them as yielding
    0 human years (no thresholds reached).
    """
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15.5, 15),     # cat as float
        ("15", 15),     # cat as str
        (None, 15),     # cat as None
        (15, 15.5),     # dog as float
        (15, "15"),     # dog as str
        (15, None),     # dog as None
        (True, 15),     # bools should not be accepted as ints here
        (15, False),
    ],
)
def test_incorrect_types_raise_typeerror(cat_age: any, dog_age: any) -> None:
    """
    Incorrect types must raise TypeError (per checklist).
    """
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
