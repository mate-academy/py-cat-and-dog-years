from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0.0, 0.0]
    assert get_human_age(10, 10) == [0.6666666666666666, 0.6666666666666666]
    assert get_human_age(14, 14) == [0.9333333333333333, 0.9333333333333333]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21.0, 17.0]


# Запуск тестов
if __name__ == "__main__":
    test_get_human_age()
    print("Все тесты пройдены успешно!")
