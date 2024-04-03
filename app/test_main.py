import pytest
from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "animal_age, first_year, second_year, each_year, expected_human_years",
    [
        (10, 15, 9, 4, 0),  # Cat age less than 1 human year
        (20, 15, 9, 4, 1),  # Cat age between 1 and 2 human years
        (30, 15, 9, 4, 3),  # Cat age more than 2 human years
        (5, 15, 9, 5, 0),  # Dog age less than 1 human year
        (16, 15, 9, 5, 1),  # Dog age between 1 and 2 human years
    ]
)
def test_convert_to_human(animal_age, first_year, second_year, each_year, expected_human_years):
    assert convert_to_human(animal_age, first_year, second_year, each_year) == expected_human_years


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (10, 5, [0, 0]),  # Cat and dog ages less than 1 human year
        (20, 16, [1, 1]),  # Cat and dog ages between 1 and 2 human years
        (30, 25, [3, 2]),  # Cat and dog ages more than 2 human years
        (5, 15, [0, 1]),  # Cat age less than 1 human year, dog age between 1 and 2 human years
        (16, 10, [1, 0]),  # Cat age between 1 and 2 human years, dog age less than 1 human year
    ]
)
def test_get_human_age(cat_age, dog_age, expected_human_ages):
    assert get_human_age(cat_age, dog_age) == expected_human_ages
