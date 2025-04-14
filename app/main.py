def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year

import pytest
from app.main import get_human_age

# Перевірка прикладів, наведених у завданні
@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age_examples(cat_age, dog_age, expected):
    """Перевірка прикладів із завдання."""
    result = get_human_age(cat_age, dog_age)
    assert result == expected


# Додаткова перевірка для впевненості, що повернені значення
# є цілими числами, а функція повертає список з двох елементів
@pytest.mark.parametrize("cat_age, dog_age", [
    (15, 14),
    (14, 15),
    (23, 22),
    (22, 23),
    (28, 27),
    (27, 28),
])
def test_get_human_age_mixed(cat_age, dog_age):
    """
    Перевірка для різних значень, що:
    - повернутий результат є списком з двох елементів;
    - обидва елементи є цілими числами.
    """
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
