from app.main import get_human_age


def test_zero_year_age_1():
    assert get_human_age(0, 0) == [0, 0]


def test_zero_year_age_2():
    assert get_human_age(14, 14) == [0, 0]


def test_one_year_age_1():
    assert get_human_age(15, 15) == [1, 1]


def test_one_year_age_2():
    assert get_human_age(23, 23) == [1, 1]


def test_two_year_age_1():
    assert get_human_age(24, 24) == [2, 2]


def test_two_year_age_2():
    assert get_human_age(27, 28) == [2, 2]


def test_more_year_age_1():
    assert get_human_age(28, 29) == [3, 3]


def test_more_year_age_2():
    assert get_human_age(100, 100) == [21, 17]
