import pytest
from app.main import get_human_age


# Тест для коректних значень віку кота та собаки
@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),             # Вік кота та собаки - 0
        (14, 9, [0, 0]),            # Молода кішка і собака
        (15, 9, [1, 0]),            # Кішка доросла, собака молода
        (20, 15, [1, 1]),           # Обидва у молодому віці
        (25, 24, [2, 2]),           # Кішка та собака у зрілому віці
        (29, 30, [3, 3]),           # Середній вік
        (30, 50, [3, 7]),           # Дорослі коти і старші собаки
        (35, 80, [4, 13]),          # Середній вік кота та старша собака
        (40, 100, [6, 17]),         # Дорослі коти і дуже старі собаки
        # Додані нові випадки
        (100, 100, [21, 17]),       # Дуже старі коти і собаки
        (249996, 199997, [62495, 39996]) # Великий вік кота та собаки
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


# Тест для некоректних значень, очікуються винятки
@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("15", 20, TypeError),      # Некоректний тип даних для віку кота (рядок замість числа)
        (15, "20", TypeError),      # Некоректний тип даних для віку собаки
    ]
)
def test_get_human_age_exceptions(cat_age, dog_age, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
