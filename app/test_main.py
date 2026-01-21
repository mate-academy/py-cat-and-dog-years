from app.main import get_human_age


def test_should_add_zeros_if_arguments_zeros():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_if_age_less_fifteen():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_if_age_equals_fifteen():
    assert get_human_age(15, 15) == [1, 1]


def test_twenty_four_years_should_convert_into_two_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_hundred_should_convert_into_twenty_one_and_seventeen():
    assert get_human_age(100, 100) == [21, 17]


def test_twenty_eight_and_twenty_nine_should_convert_into_three():
    assert get_human_age(28, 29) == [3, 3]


def test_fifty_should_convert_into_eight_and_seven():
    assert get_human_age(50, 50) == [8, 7]
