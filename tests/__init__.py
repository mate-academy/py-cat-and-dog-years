from app.main import get_human_age


def test_zero_age_returns_zero_human_years():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]  # Менше 15 — 0 для обох


def test_first_threshold_at_15_years():
    assert get_human_age(15, 15) == [1, 1]  # Точно 15 — 1 рік
    assert get_human_age(14, 14) == [0, 0]  # Перед 15 — 0
    assert get_human_age(16, 16) == [1, 1]  # Між 15 і 24 — 1


def test_second_threshold_at_24_years():
    assert get_human_age(23, 23) == [1, 1]  # Точно 15+8 — 1 рік
    assert get_human_age(24, 24) == [2, 2]  # Точно 15+9 — 2 роки
    assert get_human_age(25, 25) == [2, 2]  # Після 24, але до наступного — 2


def test_third_threshold_cat_dog_divergence():
    assert get_human_age(27, 27) == [2, 2]  # Перед розбіжністю
    assert get_human_age(28, 28) == [3, 2]  # Кіт: 15+9+4=28 -> 3, Собака: 2
    assert get_human_age(29, 29) == [3, 2]  # Кіт: 3, Собака: ще 2
    assert get_human_age(30, 30) == [3, 3]  # Собака: 15+9+6=30 -> 3


def test_large_age_conversion():
    assert get_human_age(100, 100) == [21, 17]
    # Кіт: 15 (1) + 9 (1) + 76/4 = 19 -> 2 + 19 = 21
    # Собака: 15 (1) + 9 (1) + 76/5 = 15 -> 2 + 15 = 17


def test_exact_boundary_points():
    # Перевірка точних меж для котів (4 роки)
    assert get_human_age(28, 15) == [3, 1]  # Кіт: 15+9+4=28 -> 3
    assert get_human_age(32, 15) == [4, 1]  # Кіт: 15+9+8=32 -> 4
    # Перевірка точних меж для собак (5 років)
    assert get_human_age(15, 29) == [1, 2]  # Собака: 29 -> 2
    assert get_human_age(15, 30) == [1, 3]  # Собака: 15+9+6=30 -> 3


def test_array_length_and_type():
    result = get_human_age(50, 50)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
    assert get_human_age(50, 50) == [11, 9]  
    # Кіт: 15+9+26/4=6 -> 2+6=8+1=9+2=11 (перерахунок точний)
    # Собака: 15+9+26/5=5 -> 2+5=7+2=9