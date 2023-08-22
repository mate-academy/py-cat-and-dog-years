import pytest as pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_ages",
    [
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
        "animal years under 15 equals to 0 human years",
        "first 15 pet years give 1 human year",
        "less than next 9 pet years give no more human years",
        "next 9 pet years give 1 more human year",
        "less than every 4 next cat years give no more human years",
        "every 4 next cat years give 1 extra human year",
        "every 5 next dog years give 1 extra human year",
        "further age is calculated according to the last condition",
    ]
)
def test_human_age_calculated_correctly(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list[int]
) -> None:
    assert (get_human_age(cat_age, dog_age) == expected_human_ages), \
        f"Conversion of cat ({cat_age}) and dog ({dog_age}) ages " \
        f"to human should be equal to {expected_human_ages}."


def test_size_of_array_is_correct() -> None:
    assert len(get_human_age(12, 14)) == 2


def test_return_values_are_whole_nums() -> None:
    human_age = get_human_age(17, 27)
    assert [isinstance(age, int) for age in human_age]
