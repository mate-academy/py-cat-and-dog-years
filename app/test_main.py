from app.main import get_human_age


def test_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_fourteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_twenty_three() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_twenty_seven() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_age_twenty_eight() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
