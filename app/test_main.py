from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "test_both_0",
        "test_animal_years_equal_1_human_year",
        "test_animal_years_within_1_human_year",
        "test_animal_years_within_second_human_year",
        "test_animal_years_equal_2_human_years",
        "test_cat_before_human_year_3",
        "test_cat_human_year_3_dog_still_2",
        "test_old_animals"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
