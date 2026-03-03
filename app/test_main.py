import pytest
from typing import List
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (33, 33, [4, 3]),
        (34, 34, [4, 4]),
    ],
)
def test_get_human_age_param(cat: int, dog: int, expected: List[int]) -> None:
    assert get_human_age(cat, dog) == expected


@pytest.mark.parametrize(
    "bad_cat,bad_dog",
    [
        (-1, 5),
        (5, -2),
        (-3, -3),
    ],
)
def test_negative_ages_raise_value_error(bad_cat: int, bad_dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(bad_cat, bad_dog)


@pytest.mark.parametrize(
    "bad_cat,bad_dog",
    [
        ("10", 10),
        (10, "10"),
        ("5", "5"),
        (3.5, 5),
        (5, 3.5),
        (None, 5),
    ],
)
def test_non_int_types_raise_type_error(bad_cat: object,
                                        bad_dog: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(bad_cat, bad_dog)
