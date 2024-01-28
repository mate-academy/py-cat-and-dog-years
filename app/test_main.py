from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_bellow_first_year():
    assert get_human_age(14, 14) == [0, 0]


def test_first_year():
    assert get_human_age(15, 15) == [1, 1]


def test_second_year():
    assert get_human_age(24, 24) == [2, 2]


def test_second_year_dog():
    assert get_human_age(28, 28) == [3, 2]


def test_more_years():
    assert get_human_age(100, 100) == [21, 17]


def test_age_between_first_second():
    assert get_human_age(23, 23) == [1, 1]


def test_age_between_second_third():
    assert get_human_age(27, 27) == [2, 2]
