import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (0, 0, [0, 0]),  # Both are younger than the first year
        (14, 14, [0, 0]),  # Edge case: just before the first year
        (15, 15, [1, 1]),  # Exactly the first year of life
        (23, 23, [1, 1]),  # Up to the end of the second year
        (24, 24, [2, 2]),  # Transition to the third "human" year
        (27, 27, [2, 2]),  # Still within the second "human" year
        (28, 28, [3, 2]),  # Cat gains +1 year, dog not yet
        (100, 100, [21, 17]),  # Big values
    ],
    ids=[
        "both_under_first_year",
        "both_just_before_first_year",
        "both_at_first_year",
        "both_within_second_year",
        "both_at_third_year_start",
        "both_still_second_year",
        "cat_age_plus_one_human",
        "very_old_animals",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
