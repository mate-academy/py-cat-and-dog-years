import pytest
from app.main import get_human_age, convert_to_human


def test_convert_to_human():
    assert convert_to_human(0, 15, 9, 4) == 0  # Нульовий вік дає 0
    assert convert_to_human(10, 15, 9, 4) == 0  # Менше першого року -> 0
    assert convert_to_human(15, 15, 9, 4) == 1  # Перший рік -> 1
    assert convert_to_human(24, 15, 9, 4) == 2  # Два перші роки -> 2
    assert convert_to_human(28, 15, 9, 4) == 3  # +1 додатковий рік
    assert convert_to_human(32, 15, 9, 4) == 4  # +2 додаткові роки


def test_get_human_age():
    assert get_human_age(0, 0) == [0, 0]  # Нульовий вік для обох
    assert get_human_age(15, 15) == [1, 1]  # Перший рік
    assert get_human_age(24, 24) == [2, 2]  # Другий рік
    assert get_human_age(28, 28) == [3, 3]  # Додатковий рік для обох
    assert get_human_age(32, 32) == [4, 4]  # Ще один додатковий рік


if __name__ == "__main__":
    pytest.main()
