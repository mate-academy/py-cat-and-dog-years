from app.main import get_human_age


def test_get_human_age() -> None:

    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [3, 3]  # Очікується 3, 3
    assert get_human_age(28, 28) == [3, 3]  # Очікується 3, 3
    assert get_human_age(100, 100) == [21, 17]

    # Тести для екстремальних значень
    assert get_human_age(30, 30) == [4, 3]
    assert get_human_age(50, 50) == [9, 7]
    assert get_human_age(1000, 1000) == [246, 201]

    # Тести для граничних випадків
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(16, 16) == [2, 2]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(25, 25) == [3, 3]  # Очікується 3, 3

    # Тести для випадків, коли вік менше 15 років
    assert get_human_age(0, 1) == [0, 0]
    assert get_human_age(5, 10) == [0, 0]
