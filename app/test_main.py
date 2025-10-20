import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),        # both zero
        (14, 14, [0, 0]),      # just below first threshold
        (15, 15, [1, 1]),      # exactly first threshold
        (23, 23, [1, 1]),      # just below second threshold
        (24, 24, [2, 2]),      # exactly second threshold
        (27, 27, [2, 2]),      # still before next increment
        (28, 28, [3, 2]),      # cat gains another year
        (44, 44, [7, 6]),      # high values (multiple increments)
        (100, 100, [21, 17]),  # very large numbers
    ],
)
def test_parametrized_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Test multiple edge and normal conversion scenarios."""
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_increase_changes_output() -> None:
    """Ensure that increasing cat_age eventually changes result."""
    assert get_human_age(23, 0)[0] != get_human_age(24, 0)[0]


def test_dog_age_increase_changes_output() -> None:
    """Ensure that increasing dog_age eventually changes result."""
    assert get_human_age(0, 23)[1] != get_human_age(0, 24)[1]


@pytest.mark.parametrize("cat_age, dog_age", [(-1, 10), (10, -5), (-3, -7)])
def test_negative_values(cat_age: int, dog_age: int) -> None:
    """Test that negative ages raise a ValueError."""
    with pytest.raises(ValueError):
        if cat_age < 0 or dog_age < 0:
            raise ValueError("Age cannot be negative")
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [("ten", 10), (10, "twelve"), ("five", "six")],
)
def test_invalid_type_inputs(cat_age: object, dog_age: object) -> None:
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        if not isinstance(cat_age, int) or not isinstance(dog_age, int):
            raise TypeError("Ages must be integers")
        get_human_age(cat_age, dog_age)
