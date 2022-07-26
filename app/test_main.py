from app.main import get_human_age


def test_zero_year_age_minimum():
    assert get_human_age(0, 0) == [0, 0]


def test_zero_year_age_maximum():
    assert get_human_age(14, 14) == [0, 0]


def test_first_year_age_minimum():
    assert get_human_age(15, 15) == [1, 1]


def test_first_year_age_maximum():
    assert get_human_age(23, 23) == [1, 1]


def test_second_year_age_minimum():
    assert get_human_age(24, 24) == [2, 2]


def test_second_year_age_maximum():
    assert get_human_age(27, 28) == [2, 2]


def test_more_year_age_minimum():
    assert get_human_age(28, 29) == [3, 3]


def test_more_year_age():
    assert get_human_age(100, 100) == [21, 17]
