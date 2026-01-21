import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (15, 24, [1, 2]),
        (28, 23, [3, 1]),
        (10, 30, [0, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_age",
        "before_first_conversion",
        "start_of_first_human_year",
        "before_second_conversion",
        "start_of_second_human_year",
        "before_cat_year_3_conversion",
        "start_of_cat_year_3_dog_year_2",
        "independent_check_1_cat_1_dog_2",
        "independent_check_2_cat_3_dog_1",
        "independent_check_3_cat_0_dog_3",
        "large_age_100"
    ]
)
def test_get_human_age_valid_cases(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
