from app.main import get_human_age


def test_get_human_age_zeroes() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_negative() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_get_human_age_sub_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_nineteen() -> None:
    assert get_human_age(19, 19) == [1, 1]


def test_get_human_age_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_twenty_eight() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_two_hundred() -> None:
    assert get_human_age(200, 200) == [46, 37]
