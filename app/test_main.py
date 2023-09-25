from app.main import get_human_age


def test_convert_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_exta_add_first() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_second_add() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_second_add_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_thirty_add() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
