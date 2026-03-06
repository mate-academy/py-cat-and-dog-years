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
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_years_is_zero_human_years",
        "less_than_15_years_is_zero_human_years",
        "15_years_is_one_human_year",
        "23_years_is_one_human_year",
        "24_years_is_two_human_years",
        "27_years_is_two_human_years",
        "28_years_is_three_human_years",
        "100_years_is_twenty_one_human_years"
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-5, -5),
        (1.5, 1.5),
        (None, None),
        ("ten", "ten")
    ],
    ids=[
        "negative_ages",
        "float_ages",
        "none_ages",
        "string_ages"
    ]
)
def test_get_human_age_invalid_inputs(
    cat_age: any,
    dog_age: any
) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
