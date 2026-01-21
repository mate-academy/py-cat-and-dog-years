import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),                  # Both ages are 0
        (15, 15, [1, 1]),                # First threshold
        (23, 23, [1, 1]),                # Below second threshold
        (24, 24, [2, 2]),                # Exactly at second threshold
        (28, 28, [3, 2]),                # Slightly over the second threshold
        (100, 100, [21, 17]),            # Large numbers
    ],
)
def test_get_human_age_standard_cases(
        cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected,\
        f"Failed for cat_age={cat_age}, dog_age={dog_age}"
