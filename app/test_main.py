import pytest
from app.main import get_human_age  # Импортируем функцию get_human_age

# Тесты для get_human_age
def test_get_human_age():
    # Тестируем на примерах, указанных в задании
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]

    # Дополнительные тесты для проверки
    # Для кошки 15 лет — это 1 человеческий год, 16 лет — 2 человеческих года
    assert get_human_age(16, 16) == [2, 2]
    # Для собаки 15 лет — это 1 человеческий год, 16 лет — 2 человеческих года
    assert get_human_age(16, 16) == [2, 2]
    # Для кошки 50 лет — это 10 человеческих лет
    assert get_human_age(50, 50) == [10, 10]
    # Для собаки 50 лет — это 8 человеческих лет
    assert get_human_age(50, 50) == [8, 8]


