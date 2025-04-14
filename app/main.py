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


def test_just_below_second_threshold():
    """Перевірка для 23 років: повертається [1, 1], адже ще не
    досягнуто другого порогу.
    """
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_threshold():
    """При 24 роках має повернути [2, 2]."""
    assert get_human_age(24, 24) == [2, 2]


def test_edge_between_thresholds():
    """
    Для 27 років:
    - Для кішки: (27 - 24) менше 4, отже, 2.
    - Для собаки: (27 - 24) менше 5, отже, 2.
    """
    assert get_human_age(27, 27) == [2, 2]


def test_just_above_second_threshold():
    """
    Для 28 років:
    - Для кішки: 28 - 24 = 4, отже, додається 1, всього 3.
    - Для собаки: 28 - 24 = 4, менше 5, залишається 2.
    """
    assert get_human_age(28, 28) == [3, 2]


def test_high_age():
    """
    При 100 роках має повернути [21, 17],
    згідно з прикладами завдання.
    """
    assert get_human_age(100, 100) == [21, 17]


def test_different_values():
    """
    Перевірка для різних віків:
    - Кішка 30 років: 30 >= 24, отже, кішячий вік =
      2 + ((30 - 24) // 4) = 3.
    - Собака 40 років: 40 >= 24, отже, собачий вік =
      2 + ((40 - 24) // 5) = 5.
    Очікуваний результат: [3, 5].
    """
    assert get_human_age(30, 40) == [3, 5]
