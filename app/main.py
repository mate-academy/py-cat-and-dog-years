import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1, 1, [15, 15]),
        (14, 14, [15, 15]),
        (15, 15, [24, 24]),
        (23, 23, [24, 24]),
        (24, 24, [28, 29]),
        (27, 27, [28, 29]),
        (28, 28, [32, 34]),
        (100, 100, [101, 92]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]

def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age <= 1:
        return first_year
    elif animal_age == 2:
        return first_year + second_year
    return first_year + second_year + (animal_age - 2) * each_year
