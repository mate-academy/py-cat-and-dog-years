import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years", [
        (0, 0),
        (14, 14),
        (15, 15),
        (23, 23),
        (27, 27),
        (-34, -40),
        (300, 300)
    ], ids=[
        "Test (0, 0)",
        "Test (14, 14)",
        "Test (15, 15)",
        "Test (23, 23)",
        "Test (27, 27)",
        "Negative Test (-34, -40)",
        "Test data out of normal range (300, 300)"
    ]
)
def test_get_human_age_returns_correct_value_for_dog_and_cat(
        cat_years: int,
        dog_years: int
) -> None:
    def for_test_convert_to_human(animal_age: int, each_year: int) -> int:
        first_year, second_year = 15, 9
        if animal_age < 15:
            return 0
        if animal_age < first_year + second_year:
            return 1
        return 2 + (animal_age - first_year - second_year) // each_year

    cat_years_convert_to_human = for_test_convert_to_human(cat_years, 4)
    dog_years_convert_to_human = for_test_convert_to_human(dog_years, 5)
    assert (
        get_human_age(cat_years, dog_years)
        == [
            cat_years_convert_to_human,
            dog_years_convert_to_human
        ]
    )


@pytest.mark.parametrize(
    "cat_years,dog_years", [
        ("22", 34),
        (12, "45"),
        ("22", "45")
    ], ids=[
        "Cat-> str='22', Dog-> int=34",
        "Cat-> int=12, Dog-> str='45'",
        "Cat-> str='22', Dog-> str='45'",
    ]
)
def test_get_human_age_returns_type_error_for_dog_and_cat(
        cat_years: int | str,
        dog_years: int | str
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
