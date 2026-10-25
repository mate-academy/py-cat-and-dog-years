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
        (29, 29, [3, 3]),
        (32, 32, [4, 3]),
        (34, 34, [4, 4]),
    ],
    ids=[
        "ages_are_zero",
        "before_first_human_year",
        "ages_are_fifteen",
        "upper_edge_of_second_range",
        "ages_are_twenty_four",
        "before_third_human_year",
        "cat_three_dog_still_two",
        "dog_three_after_five_years_period",
        "cat_four_dog_still_three",
        "dog_four_after_second_five_years_period",
    ],
)
def test_human_age(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
