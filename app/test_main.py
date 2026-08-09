from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_twenty_eight_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_one_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_fourteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]
