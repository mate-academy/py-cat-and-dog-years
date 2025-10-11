import pytest
from app.main import get_human_age

# This file tests the behavior of get_human_age()
# It verifies correct results, error handling, type safety, and rounding logic.


#  Main correctness test – checks all given example cases
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),          # both zero years -> both zero human years
        (14, 14, [0, 0]),        # still under first threshold
        (15, 15, [1, 1]),        # first threshold reached
        (23, 23, [1, 1]),        # still same range
        (24, 24, [2, 2]),        # second threshold reached
        (27, 27, [2, 2]),        # still same human years
        (28, 28, [3, 2]),        # cat gets extra year before dog
        (100, 100, [21, 17]),    # large numbers, final expected values
    ]
)
def test_get_human_age_returns_expected_values(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    """Check that the function returns the correct
    [cat, dog] human year values."""
    result = get_human_age(cat_age, dog_age)
    assert result == expected


# Structural test – ensures the output is a list of two integers
def test_get_human_age_returns_two_integers() -> None:
    """Verify that the result is a list of two integers."""
    result = get_human_age(14, 14)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


# Boundary test – dog’s human age transition from 2 → 3 years
def test_get_human_age_dog_boundary_between_2_and_3_human_years() -> None:
    """Ensure the dog's human age increments
       exactly at the correct boundary."""
    result_28 = get_human_age(0, 28)
    result_29 = get_human_age(0, 29)
    assert result_28[1] == 2  # before threshold
    assert result_29[1] == 3  # after threshold


# Negative values – must raise ValueError
@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),    # negative cat age
        (10, -1),    # negative dog age
        (-1, -10),   # both negative
    ]
)
def test_get_human_age_negative_values_raise_value_error(
        cat_age: int,
        dog_age: int
) -> None:
    """Negative ages are invalid – should raise ValueError."""
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


# Invalid input types – must raise ValueError
@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("cat", 10),       # string instead of int
        (5, "dog"),        # string for dog
        (5.5, 10),         # float for cat
        (10, 4.5),         # float for dog
        (None, 14),        # None for cat
        (15, None),        # None for dog
        ([1, 2], 4),       # list instead of int
    ]
)
def test_get_human_age_raises_error_when_given_invalid_input(
        cat_age: int,
        dog_age: int
) -> None:
    """Non-integer or invalid data types should raise ValueError."""
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


# Truncation test – ensures fractional human years are discarded
def test_get_human_age_truncates_fractional_years() -> None:
    """Confirm that all human years are whole numbers (no decimals)."""
    cat_age = 27
    dog_age = 28
    result = get_human_age(cat_age, dog_age)
    assert all(isinstance(x, int) for x in result)  # both integers
    assert all(x == int(x) for x in result)         # no fractions returned
