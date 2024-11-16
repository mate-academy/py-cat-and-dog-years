import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),  # Both ages are zero
        (14, 14, [0, 0]),  # Both ages below first threshold
        (15, 15, [1, 1]),  # Both ages exactly at first threshold
        (23, 23, [1, 1]),  # Both ages between first and second thresholds
        (24, 24, [2, 2]),  # Both ages exactly at second threshold
        (27, 27, [2, 2]),  # Both ages between 1 threshold and 2 conv
        (28, 28, [3, 2]),  # Past second threshold: additional years for cat
        (33, 33, [4, 3]),  # Higher ages, calculate properly
        (100, 100, [21, 17]),  # Large values for both
    ],
)
def test_get_human_age_valid_inputs(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    """Test get_human_age with valid inputs."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),  # Negative cat age
        (10, -1),  # Negative dog age
        (-5, -5),  # Both negative
    ],
)
def test_get_human_age_negative_ages(cat_age: int, dog_age: int) -> None:
    """Test get_human_age with negative ages."""
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 10),  # String instead of integer for cat age
        (10, "ten"),  # String instead of integer for dog age
        (10.5, 20),  # Float for cat age
        (20, 10.5),  # Float for dog age
        (None, 10),  # None for cat age
        (10, None),  # None for dog age
    ],
)
def test_get_human_age_invalid_data_types(cat_age: any, dog_age: any) -> None:
    """Test get_human_age with invalid data types."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
