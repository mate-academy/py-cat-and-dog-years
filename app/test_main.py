import pytest
from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
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
)
def test_correctly_converted_animals_age_to_human(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "animal_age,first_year,second_year,each_year,result",
    [
        (14, 9, 4, 5, 2),
        (15.1, 9, 4, 5, 2),
        (15, 8, 4, 5, 2),
        (15, 9.1, 4, 5, 2),
        (15, 9, 3, 4, 2),
        (15, 9, 4.1, 5.1, 2),
    ],
)
def test_correctly_converted_one_animal_age_to_human(
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year: int,
        result: int
) -> None:
    assert convert_to_human(
        animal_age,
        first_year,
        second_year,
        each_year
    ) == result
