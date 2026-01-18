import pytest
from app.main import get_human_age


def test_not_int_values() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "3")


def test_below_zero_values() -> None:
    with pytest.raises(ValueError):
        get_human_age(-10, 0)


def test_unrealistic_values() -> None:
    with pytest.raises(OverflowError):
        get_human_age(1000, 1000)


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "All zeroes",
        "All less than 15",
        "All 15",
        "All 16",
        "All 23",
        "All 24",
        "All 25",
        "27 and 28",
        "28 and 29",
        "All 100",
    ]
)
def test_calculation_with_diff_val(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        f"Age values from {cat_age} and {dog_age} should be equal to {result}"
