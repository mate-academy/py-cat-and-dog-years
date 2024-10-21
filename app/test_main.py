import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
"cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),                  # Test 1: Both cat and dog have 0 years
        (14, 14, [0, 0]),                # Test 2: Both cat and dog have ages below 15
        (15, 15, [1, 1]),                # Test 3: Both cat and dog have exactly 15 years
        (23, 23, [1, 1]),                # Test 4: Both cat and dog have ages between 15 and 24
        (24, 24, [2, 2]),                # Test 5: Both cat and dog have exactly 24 years
        (27, 27, [2, 2]),                # Test 6: Both cat and dog have exactly 27 years
        (28, 28, [3, 2]),                # Test 7: Both cat and dog have exactly 28 years
        (100, 100, [21, 17]),            # Test 8: Both cat and dog have 100 years (extreme case)
        (28, 14, [3, 0]),                # Test 9: Dog's age is below 15, cat's age is 28
        (14, 28, [0, 2]),                # Test 10: Cat's age is below 15, dog's age is 28
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, f"Expected {expected}, but got {result}"