import pytest
from app import main


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (-1, 0, [0, 0]),
    (0, -1, [0, 0]),
    (-10, -10, [0, 0]),
])
def test_get_human_age_negative_ages(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),  # Just below threshold
    (15, 15, [1, 1]),  # At threshold
    (23, 23, [1, 1]),  # Just below threshold
    (24, 24, [2, 2]),  # At threshold
    (27, 27, [2, 2]),  # Just below next increment
    (28, 28, [3, 2]),  # First increment for cat, dog stays same
])
def test_get_human_age_boundary_conditions(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    """Test boundary pairs to verify threshold behavior."""
    assert main.get_human_age(cat_age, dog_age) == expected
