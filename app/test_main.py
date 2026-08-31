import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Zero years
        (0, 0, [0, 0]),
        # Before reaching the first threshold (15 years)
        (14, 14, [0, 0]),
        # First threshold reached (15 years = 1 human year)
        (15, 15, [1, 1]),
        # Right before second threshold (15 + 8 = 23 years)
        (23, 23, [1, 1]),
        # Second threshold reached (15 + 9 = 24 years = 2 human years)
        (24, 24, [2, 2]),
        # Edge of step increments (Cat +4, Dog +5)
        (27, 27, [2, 2]),
        # Cat reaches 3rd year at 28 (24 + 4), Dog stays at 2 until 29 (24 + 5)
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        # High age conversion test
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_conversions(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_ages_calculated_independently() -> None:
    # 28 cat years -> 3 human years, 15 dog years -> 1 human year
    assert get_human_age(28, 15) == [3, 1]
    # 14 cat years -> 0 human years, 100 dog years -> 17 human years
    assert get_human_age(14, 100) == [0, 17]
