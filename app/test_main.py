from app.main import get_human_age


def test_age_under_first_year_convert():
    assert get_human_age(14, 14) == [0, 0]


def test_age_more_than_first_year_convert_and_less_than_second_year():
    assert get_human_age(23, 23) == [1, 1]


def test_age_more_than_second_year_and_less_than_third_year():
    assert get_human_age(25, 25) == [2, 2]


def test_age_more_than_third_year():
    assert get_human_age(40, 50) == [6, 7]
