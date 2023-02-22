from app.main import get_human_age


def test_age_is_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_15_years():
    assert get_human_age(14, 14) == [0, 0]


def test_first_15_years():
    assert get_human_age(15, 23) == [1, 1]


def test_next_9_years():
    assert get_human_age(25, 25) == [2, 2]


def test_every_next_5_years():
    assert get_human_age(28, 28) == [3, 2]
