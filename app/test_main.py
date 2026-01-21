from app.main import get_human_age


def test_zero_ages() -> None:
    """Тест з нульовими віками"""
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    """Тест з віком менше 15 років (перший поріг)"""
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(1, 1) == [0, 0]
    assert get_human_age(10, 10) == [0, 0]


def test_first_threshold_exactly() -> None:
    """Тест з віком рівно 15 років"""
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshold_range() -> None:
    """Тест з віком між 15 і 24 роками"""
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(20, 20) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_second_threshold_exactly() -> None:
    """Тест з віком рівно 24 роки (15 + 9)"""
    assert get_human_age(24, 24) == [2, 2]


def test_third_threshold_range() -> None:
    """Тест з віком після 24 років"""
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_cat_dog_difference() -> None:
    """Тест де коти і собаки мають різний вік у людських роках"""
    # Кіт: 28 років = 1 (за 15) + 1 (за 9) + 1 (за 4) = 3 роки
    # Собака: 28 років = 1 (за 15) + 1 (за 9) + 0 (недостатньо для 5) = 2
    assert get_human_age(28, 28) == [3, 2]


def test_cat_multiple_extra_years() -> None:
    """Тест з котами, що мають багато додаткових років"""
    # Кіт: 32 роки = 1 (за 15) + 1 (за 9) + 2 (за 8, кожні 4) = 4 роки
    # Собака: 32 роки = 1 (за 15) + 1 (за 9) + 1 (за 5, залишок 3) = 3
    assert get_human_age(32, 32) == [4, 3]


def test_dog_multiple_extra_years() -> None:
    """Тест з собаками, що мають багато додаткових років"""
    # Кіт: 36 років = 1 (за 15) + 1 (за 9) + 3 (за 12, кожні 4) = 5 років
    # Собака: 36 років = 1 (за 15) + 1 (за 9) + 2 (за 10, кожні 5) = 4
    assert get_human_age(36, 36) == [5, 4]


def test_large_ages() -> None:
    """Тест з великими віками"""
    assert get_human_age(100, 100) == [21, 17]


def test_edge_cases_cat_thresholds() -> None:
    """Тест граничних випадків для котів"""
    # Кіт: 28 років = 15 + 9 + 4 = 3 роки
    assert get_human_age(28, 0) == [3, 0]
    # Кіт: 31 років = 15 + 9 + 4 + 3 (недостатньо для наступних 4) = 3
    assert get_human_age(31, 0) == [3, 0]
    # Кіт: 32 роки = 15 + 9 + 4 + 4 = 4 роки
    assert get_human_age(32, 0) == [4, 0]


def test_edge_cases_dog_thresholds() -> None:
    """Тест граничних випадків для собак"""
    # Собака: 29 років = 15 + 9 + 5 = 3 роки
    assert get_human_age(0, 29) == [0, 3]
    # Собака: 33 роки = 15 + 9 + 5 + 4 (недостатньо для наступних 5) = 3
    assert get_human_age(0, 33) == [0, 3]
    # Собака: 34 роки = 15 + 9 + 5 + 5 = 4 роки
    assert get_human_age(0, 34) == [0, 4]


def test_different_ages() -> None:
    """Тест з різними віками котів і собак"""
    # Кіт: 50 років, Собака: 60 років
    # Кіт: 1 (15) + 1 (9) + 6 (26/4) = 8 років
    # Собака: 1 (15) + 1 (9) + 7 (36/5) = 9 років
    assert get_human_age(50, 60) == [8, 9]


def test_boundary_values() -> None:
    """Тест граничних значень"""
    # Перевірка точних порогів
    assert get_human_age(15, 15) == [1, 1]  # Перший поріг
    assert get_human_age(24, 24) == [2, 2]  # Другий поріг
    assert get_human_age(28, 29) == [3, 3]  # Третій поріг для кота і собаки


def test_very_small_ages() -> None:
    """Тест з дуже малими віками"""
    assert get_human_age(1, 2) == [0, 0]
    assert get_human_age(5, 10) == [0, 0]


def test_asymmetric_ages() -> None:
    """Тест з асиметричними віками"""
    # Один старий, один молодий
    assert get_human_age(100, 15) == [21, 1]
    assert get_human_age(15, 100) == [1, 17]
