import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Standard cases
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # Boundary transitions
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        # Out-of-normal-range: Negative ages (Evaluating to 0 human years)
        (-1, 5, [0, 0]),
        (5, -1, [0, 0]),
        (-10, -10, [0, 0]),
        # Out-of-normal-range: Very large ages
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
        # Incorrect types: Floats (Should be safely calculated or truncated)
        (15.5, 15, [1, 1]),
        (24, 24.9, [2, 2]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
