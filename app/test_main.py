from typing import Any

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "test cat age and dog age are both years",
        "test cat age and dog age equal one year",
        "test cat age and dog age equal two years",
        "test value slightly less the first limit",
        "test between first and second limit",
        "test on the border of the next block without cat",
        "test on the verge of transition to next block cat gets year",
        "test large number for checking multiple block repetitions",
    ]
)
def test_valid_values(cat: int, dog: int, result: list[int]) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog",
    [
        (0, -5),
        (-4, 2),
        (-7, -7),
    ],
    ids=[
        "test dog's age is negative",
        "test cat's age is negative",
        "test all age is negative"
    ]
)
def test_negative_age_raises_type_error(cat: int, dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)


@pytest.mark.parametrize(
    "cat, dog",
    [
        ("str", [0, 0, 0]),
        (12.5, 3),
        (3, "5"),
        ("5", None),
    ],
    ids=[
        "test input cat age is str and dog age is list",
        "test cat age is double",
        "test dog age is str",
        "test cat age is str and dog age is None",
    ],
)
def test_invalid_input(cat: Any, dog: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
