from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
    ]
)
def test_age_below_15(cat_age: int,
                      dog_age: int,
                      expected: list
                      ) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2])
    ]
)
def test_boundary_age_between_15_and_24(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 28, [3, 2]),
        (29, 30, [3, 3]),
        (50, 50, [8, 7]),
        (100, 100, [21, 17])
    ]
)
def test_last_boundary_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_only_one_age_are_boundary() -> None:
    assert get_human_age(24, 14) == [2, 0]
    assert get_human_age(14, 24) == [0, 2]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("5", 10),      # string замість int
        (10, "7"),      # string
        (None, 10),     # None
        (10, None),     # None
        ([1, 2], 5),    # list
        (3.5, 4),       # float
        (5, {"a": 1}),  # dict
    ],
)
def test_get_human_age_invalid_type_raises_type_error(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -10),
    ],
)
def test_get_human_age_negative_input_raises_value_error(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
