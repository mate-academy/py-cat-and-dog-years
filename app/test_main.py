from app.main import get_human_age


def test_with_arguments_equal_zero_return_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_arguments_both_less_15_return_zero():
    assert get_human_age(14, 14) == [0, 0]


def test_arguments_both_15_return_1():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_when_arguments_more_than():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_arguments_equal_two_human_year():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_when_arguments_more_then_two_less_3():
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_3_human_years():
    assert get_human_age(28, 29) == [3, 3]


def test_with_old_animals():
    assert get_human_age(100, 100) == [21, 17]