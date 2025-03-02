import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),  # Edge case: Both ages are zero
        (14, 14, [0, 0]),  # Just below the first human year threshold
        (15, 15, [1, 1]),  # First human year
        (23, 23, [1, 1]),  # Still in the first human year range
        (24, 24, [2, 2]),  # Transition to the second human year
        (27, 27, [2, 2]),  # Still in the second human year range
        (28, 28, [3, 2]),  # Cat gets an additional year before dog
        (100, 100, [21, 17]),  # Large age test
        (15, 0, [1, 0]),  # Only cat has age reaching human year
        (0, 15, [0, 1]),  # Only dog has age reaching human year
        (24, 15, [2, 1]),  # Different ages, both converted
        (15, 24, [1, 2]),  # Different ages, reversed case
        (-5, 20, [0, 1]),  # Edge case: Negative cat age
        (20, -10, [1, 0]),  # Edge case: Negative dog age
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
