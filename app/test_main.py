import pytest
from typing import List
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
    assert all(isinstance(x, int) for x in result)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("5", 5),
        (5, "5"),
        (None, 5),
        (5, None),
    ],
)
def test_get_human_age_invalid_type_raises(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (3.5, 5, get_human_age(int(3.5), 5)),
        (5, 3.5, get_human_age(5, int(3.5))),
    ],
)
def test_get_human_age_with_float_inputs(
    cat_age: float, dog_age: float, expected: List[int]
) -> None:

    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
    assert result == expected
