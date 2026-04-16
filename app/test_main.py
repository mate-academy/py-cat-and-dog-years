import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Threshold 1: 15 years
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),

        # Threshold 2: 24 years (15 + 9)
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),

        # Threshold 3: Cat increments at 28 (24 + 4)
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),

        # Threshold 3: Dog increments at 29 (24 + 5)
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),

        # Large scale test
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_negative_input() -> None:
    # Ensures your tests catch if the function handles negatives poorly
    assert get_human_age(-1, -1) == [0, 0]
