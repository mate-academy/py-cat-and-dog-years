from app.main import get_human_age, convert_to_human


def test_one_year_or_less():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_two_years():
    assert get_human_age(24, 24) == [2, 2]


def test_second_year_and_greater():
    assert get_human_age(30, 30) == [3, 3]
