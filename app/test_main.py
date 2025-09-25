import pytest
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
        (100, 100, [21, 17]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (16, 16, [1, 1]),
        (34, 34, [4, 4]),
    ]
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    """
    Test get_human_age for various boundary values, large numbers,
    and single-animal age effects.
    """
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        -1,
        -10,
        -100,
        3.5,
        "cat",
        None,
    ]
)
def test_get_human_age_invalid_type(
    invalid_input: int | float | str | None
) -> None:
    """
    Ensure get_human_age raises TypeError or ValueError on invalid input.
    """
    with pytest.raises((TypeError, ValueError)):
        get_human_age(invalid_input, invalid_input)
