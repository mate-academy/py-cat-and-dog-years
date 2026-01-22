import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (50, 50, [8, 7]),
        (28, 28, [3, 2]),
        (70, 35, [13, 4]),
        (35, 70, [4, 11]),
        (100, 100, [21, 17]),
        (9999, 9999, [2495, 1997])
    ]
)
def test_get_human_age(
        cat_age: int, dog_age: int, expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("10", 10, TypeError),
        (20, "20", TypeError),
        (35, bool, TypeError),
        (44, None, TypeError),
    ]
)
def test_type_error_func_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
