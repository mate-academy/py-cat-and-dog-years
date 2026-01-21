import pytest
from app import main


# Перевірка загальних тестів для кішки та собаки
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (35, 35, [4, 4]),  # Перевірка для 35 років
        (100, 100, [21, 17]),  # Перевірка для 100 років
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected, (f"Помилка при cat_age={cat_age}, "
                                f"dog_age={dog_age}, отримано {result}")


# Перевірка лише для віку кішки
@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (60, [11, 0]),
        (100, [21, 0]),
    ],
)
def test_only_cat_age(cat_age: int, expected: list) -> None:
    result = main.get_human_age(cat_age, 0)
    assert result == expected, (f"Перевірка конвертації "
                                f"лише віку кішки для cat_age={cat_age}")


# Перевірка лише для віку собаки
@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (60, [0, 9]),  # Очікується 9 для собаки
        (100, [0, 17]),  # Велике значення
    ],
)
def test_only_dog_age(dog_age: int, expected: list) -> None:
    result = main.get_human_age(0, dog_age)
    assert result == expected, (f"Перевірка конвертації "
                                f"лише віку собаки для dog_age={dog_age}")


# Тести для граничних умов
@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 9, [1, 0]),  # Граничні значення для кожної тварини
        (28, 28, [3, 2]),
    ],
)
def test_boundary_conditions(cat_age: int, dog_age: int,
                             expected: list) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected, (f"Перевірка граничних "
                                f"умов для cat_age={cat_age}, "
                                f"dog_age={dog_age}")
