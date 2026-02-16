import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    (-15, -5, [0, 0]),  # Тест на від'ємні числа
    (0, 0, [0, 0]),  # Менше 15
    (14, 14, [0, 0]),   # Граничне значення < 15
    (15, 15, [1, 1]),   # Перший поріг
    (23, 23, [1, 1]),   # Граничне значення < 24
    (24, 24, [2, 2]),   # Другий поріг
    (27, 27, [2, 2]),   # Не вистачає до наступного кроку кота
    (27, 28, [2, 2]),   # Не вистачає до наступного кроку кота та собаки
    (28, 28, [3, 2]),   # Наступний крок для кота
    (28, 29, [3, 3]),   # Рівно наступний крок (24+4 для кота, 24+5 для собаки)
    (100, 100, [21, 17]),  # Великі значення
    (10**6, 10**6, [249996, 199997]),  # Тест на дуже великі числа
])
def test_get_human_age(cat_years: int, dog_years: int, expected: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected


def test_should_truncate_float_values() -> None:
    # 15.9 має стати 15 -> результат [1, 1]
    # 23.9 має стати 23 -> результат [1, 1]
    assert get_human_age(15.9, 23.9) == [1, 1]


# Новий тест: Перевірка неправильних типів даних
@pytest.mark.parametrize("bad_cat, bad_dog, expected_exception", [
    ("abc", 15, ValueError),      # Рядок неможливо перетворити на int
    (None, 15, TypeError),       # None викликає TypeError при int(None)
    ([], 15, TypeError),         # Список викликає TypeError
    (object(), 15, TypeError),   # Об'єкт викликає TypeError
])
def test_should_raise_error_on_invalid_types(bad_cat: int,
                                             bad_dog: int,
                                             expected_exception: list) -> None:
    with pytest.raises(expected_exception):
        get_human_age(bad_cat, bad_dog)
