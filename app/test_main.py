from typing import List


def convert_to_human(animal_age: int, first_year: int, second_year: int) -> int:
    """Convert animal age to human-equivalent years based on thresholds.

    Args:
        animal_age: Age of the animal in years
        first_year: Age threshold for first human year
        second_year: Age threshold for second human year

    Returns:
        Human-equivalent age
    """
    if animal_age < first_year:
        return 0
    elif animal_age < first_year + second_year:
        return 1
    else:
        # First 2 years count differently, then 4 human years per animal year
        return 2 + (animal_age - (first_year + second_year)) // 4


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    """Convert cat and dog ages to human-equivalent ages.

    Args:
        cat_age: Age of the cat in years
        dog_age: Age of the dog in years

    Returns:
        List containing [human_cat_age, human_dog_age]

    Raises:
        TypeError: If either cat_age or dog_age is negative
    """
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise TypeError("Ages cannot be negative")

    # Cat: 15 years = 1st human year, 9 years = 2nd human year
    human_cat_age = convert_to_human(cat_age, 15, 9)
    # Dog: 15 years = 1st human year, 9 years = 2nd human year
    human_dog_age = convert_to_human(dog_age, 15, 9)

    return [human_cat_age, human_dog_age]


# Test file
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),  # Zero age case
        (14, 14, [0, 0]),  # Below first threshold
        (15, 15, [1, 1]),  # At first threshold
        (23, 23, [1, 1]),  # Below second threshold
        (24, 24, [2, 2]),  # At second threshold
        (27, 27, [2, 2]),  # After second threshold
        (28, 28, [3, 2]),  # Different conversions
        (100, 100, [21, 17]),  # Large ages
    ]
)
def test_age_conversion(cat_age: int, dog_age: int, expected: List[int]) -> None:
    """Test various age conversion scenarios."""
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_ages() -> None:
    """Test that negative ages raise TypeError."""
    with pytest.raises(TypeError):
        get_human_age(-1, 5)
    with pytest.raises(TypeError):
        get_human_age(5, -1)
    with pytest.raises(TypeError):
        get_human_age(-1, -1)