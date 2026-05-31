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
        (28, 29, [3, 3]),

        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_years",
        "just_before_1_human_year",
        "exactly_1_human_year",
        "just_before_2_human_years",
        "exactly_2_human_years",
        "cat_boundary_for_2_years",
        "cat_reaches_3_years_dog_stays_2",
        "dog_reaches_3_years",
        "large_values_100"
    ]
)
def test_get_human_age_standard_cases(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)

    assert result == expected, f"Expected {expected}, but got {result}"
    assert isinstance(result, list), "The result must be a list (array)"
    assert len(result) == 2, "The result must contain exactly 2 elements"


def test_should_return_zeros_for_ages_less_than_fifteen() -> None:
    result = get_human_age(5, 10)
    assert result == [0, 0]


def test_cat_and_dog_ages_are_evaluated_independently() -> None:
    assert get_human_age(15, 28) == [1, 2]
    assert get_human_age(28, 15) == [3, 1]


def test_discard_remainder_property() -> None:
    result = get_human_age(27, 33)
    assert result == [2, 3]
