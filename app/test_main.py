from app.main import get_human_age


def test_when_human_age_equal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_when_human_age_less_then_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_when_human_age_equal_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_when_human_age_equal_twenty_three() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_when_human_age_equal_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_when_human_age_equal_one_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
