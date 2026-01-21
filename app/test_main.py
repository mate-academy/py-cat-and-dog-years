import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (10, 8, [0, 0]),  # Both ages are less than 15
        (15, 15, [1, 1]),  # Boundary case: age equals 15
        (20, 23, [1, 1]),  # Age between 15 and 24
        (24, 24, [2, 2]),  # Boundary case: age equals 24
        (28, 28, [3, 2]),  # Age 28: checks logic for 3 human years
        (29, 29, [3, 3]),  # Age 29: checks logic for 3 human years
        (50, 50, [8, 7]),  # Cats age faster than dogs after a certain point
        (0, 0, [0, 0]),  # Edge case: age is 0
        (-5, -5, [0, 0]),  # Negative ages
        (100, 100, [21, 17]),  # Very large ages
    ],
)
def test_get_human_age(cat_age, dog_age, expected):
    """Tests correct age conversion for cats and dogs."""
    assert get_human_age(cat_age, dog_age) == expected, f"Failed for cat_age={cat_age}, dog_age={dog_age}"


@pytest.mark.parametrize(
    "cat_age, dog_age, exception_type",
    [
        ("15", 15, TypeError),  # Invalid type: string for cat_age
        (15, "15", TypeError),  # Invalid type: string for dog_age
        (None, 15, TypeError),  # Invalid type: None for cat_age
        (15, None, TypeError),  # Invalid type: None for dog_age
    ],
)
def test_get_human_age_invalid_inputs(cat_age, dog_age, exception_type):
    """Tests that the function raises exceptions for invalid inputs."""
    with pytest.raises(exception_type):
        get_human_age(cat_age, dog_age)
