import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (75, 50, [14, 7])
    ],
    ids=[
        "Test check number of arguments that are returned",
        "Test return value of first human year",
        "Test return value of second_human year if input values is 15",
        "Test return value of third_human year if input values is 23",
        "Test return value of third_human year if input values is 24",
        "Test return value of human_year if input values is 27",
        "Test return fourth human year for and cat third human year for dog",
        "Test return value of human_year if input values is 29",
        "Test return value of human_year if input values is 100",
        "Test return value of human_year if input values is different"
    ]
)
def test_check_human_age_that_are_returned(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == human_age), \
        (f"Human age for cat age {cat_age} should be equal to {human_age[0]}, "
         f"human age for dog age {dog_age} should be equal to {human_age[1]}")


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("6", "18", TypeError),
        (3.5, 4.5, TypeError),
        (None, None, TypeError),
        ([], [5], TypeError),
        ({16}, {}, TypeError),
        (-2, -5, ValueError)
    ],
    ids=[
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect value of input data"
    ]
)
def test_raising_errors(
        cat_age: int,
        dog_age: int,
        expected_error: TypeError | ValueError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
