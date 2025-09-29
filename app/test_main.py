import pytest
from typing import List, Optional, Union
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
        (29, 29, [3, 3]),
        (30, 30, [3, 3]),
        (50, 50, [8, 7]),
        (60, 60, [11, 9]),
        (100, 100, [21, 17]),
        (16, 16, [1, 1]),
        (24, 23, [2, 1]),
        (23, 24, [1, 2]),
        (-1, -1, [0, 0]),
        (10_000, 10_000, [2496, 1997]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    result = get_human_age(cat_age, dog_age)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result), "All elements must be int"

    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("5", 5),
        (5, "5"),
        (None, 5),
        (5, None),
        (3.5, 5),
        (5, 3.5),
    ],
)
def test_get_human_age_invalid_type_outputs(
    cat_age: Optional[Union[int, str, float]],
    dog_age: Optional[Union[int, str, float]],
) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
    except Exception:
        return

    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result list must have two elements"
    assert all(isinstance(x, int) for x in result), \
        "Result must only contain int"
