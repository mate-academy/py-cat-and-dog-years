import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Zero and negative values
        (0, 0, [0, 0]),
        (-1, -5, [0, 0]),
        # Below first threshold (0 to 14)
        (14, 14, [0, 0]),
        # First threshold reached (15 cat/dog years = 1 human year)
        (15, 15, [1, 1]),
        # Between first and second threshold (15 to 23)
        (23, 23, [1, 1]),
        # Second threshold reached (24 cat/dog years = 2 human years)
        (24, 24, [2, 2]),
        # Cat boundary for 3 human years (24 + 4 = 28)
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        # Dog boundary for 3 human years (24 + 5 = 29)
        (28, 29, [3, 3]),
        # Larger numbers and higher bounds
        (100, 100, [21, 17]),
        (100, 28, [21, 2]),
    ],
    ids=[
        "zeros",
        "negative_ages",
        "under_15_years",
        "first_threshold_15_years",
        "under_24_years",
        "second_threshold_24_years",
        "cat_27_dog_27_years",
        "cat_28_dog_28_years",
        "dog_29_years",
        "large_ages_100",
        "different_ages",
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
