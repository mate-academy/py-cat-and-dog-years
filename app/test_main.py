import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years_to_convert, dog_years_to_convert, expected_years",
    [
        (0, 0, [0, 0]),
        (24, 24, [2, 2]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (14, 14, [0, 0]),
        (1211213313, 11133131313, [302803324, 2226626259]),
        (-12, -22, [0, 0])
    ],
    ids=[
        "should return [0, 0] if both years are 0",
        "should return [2, 2] for cat and dog both 24 years",
        "should return [1, 1] for cat and dog both 15 years",
        "should return [1, 1] for cat and dog both 23 years",
        "should return [3, 2] for cat and dog both 28 years",
        "should return [21, 17] for cat and dog both 100 years",
        "should return [0, 0] for cat and dog age, if age < 15",
        "should return correct values for big ages",
        "should return [0, 0], if age < 0"
    ]
)
def test_of_converting_animals_years_to_people_years(
        cat_years_to_convert: int,
        dog_years_to_convert: int,
        expected_years: tuple
) -> None:
    assert get_human_age(
        cat_years_to_convert,
        dog_years_to_convert
    ) == expected_years


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_error",
    [
        ([1, 2, 3, 4], (22, 22), TypeError),
        ("hi", 13, TypeError)
    ],
    ids=[
        "all ages should have correct type: int",
        "all ages should be type: int"
    ]
)
def teat_first(
        cat_years: int,
        dog_years: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_years, dog_years)


def test_output_does_not_change_with_previous_value() -> None:
    cat_years, dog_years = 10, 5

    initial_human_age = get_human_age(cat_years, dog_years)
    human_age_after_repeat = get_human_age(cat_years, dog_years)

    assert human_age_after_repeat == initial_human_age
