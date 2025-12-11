from app.main import get_human_age


def test_get_human_age_when_zeroes():
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_when_less_than_15_years():
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_when_less_than_24_years():
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_when_more_than_27_years():
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_when_more_than_40_years():
    assert get_human_age(40, 40) == [6, 5]
