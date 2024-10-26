import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1, 1, [15, 15]),    # Вік 1 рік відповідає 15 людським рокам
        (14, 14, [15, 15]),  # Для віку тварини в 14 років буде мінімальне значення - 15 років
        (15, 15, [24, 24]),  # Вік 15 років відповідає 24 людським рокам
        (23, 23, [24, 24]),  # Вік 23 роки буде еквівалентний 24 людським
        (24, 24, [28, 29]),  # Вік 24 роки - 28 років для кота і 29 для собаки
        (27, 27, [28, 29]),  # Вік 27 років відповідає 28 людським для кота, 29 - для собаки
        (28, 28, [32, 34]),  # Вік 28 років - 32 роки для кота і 34 для собаки
        (100, 100, [101, 92]) # Вік 100 років - 101 людський для кота, 92 для собаки
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
    if animal_age == 1:
        return first_year
    elif animal_age == 2:
        return first_year + second_year
    return first_year + second_year + (animal_age - 2) * each_year
