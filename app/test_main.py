import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (10, 10, [0, 0]),
        (15, 15, [1, 1]),
        (20, 20, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (40, 40, [6, 5]),
        (16, 40, [1, 5]),
        (40, 16, [6, 1]),
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat_and_dog_under_first_year",
        "cat_and_dog_at_first_year",
        "cat_and_dog_between_first_and_second_year",
        "cat_and_dog_at_second_year",
        "cat_and_dog_after_second_year",
        "cat_and_dog_long_life",
        "cat_16_dog_40",
        "cat_40_dog_16",
        "newborn_cat_and_dog",
        "maximum_years",
    ]
)
def test_get_human_age(
        cat_age: int, dog_age: int, expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
