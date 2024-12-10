from app.main import get_human_age


def test_zeros_cats_and_dogs_ages_in_human_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_check_correctly_converted_less_fifteen_cats_and_dogs_years_in_human_age():
    assert get_human_age(14, 14) == [0, 0]


def test_check_correctly_converted_in_first_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_check_correctly_converted_in_second_human_year():
    assert get_human_age(24, 24) == [2, 2]


def test_check_correctly_converted_cats_and_dogs_years_in_third_and_more_human_years():
    assert get_human_age(28, 28) == [3, 2]


def test_very_large_cats_and_dogs_ages_in_human_ages():
    assert get_human_age(100, 100) == [21, 17]
