from app.main import get_human_age


def test_age_should_be_a_whole_number_of_years_rounded_to_lower_number():
    assert get_human_age(89, 88) == [18, 14]


def test_first_year():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]


def test_second_year():
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_each_next_year():
    assert get_human_age(28, 29) == [3, 3]
