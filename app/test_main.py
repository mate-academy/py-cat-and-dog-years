from app.main import get_human_age


def test_return_zeros_when_age_is_less_then_15():
    assert get_human_age(14, 14) == [0, 0]


def test_return_zeros_when_input_is_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_return_zeros_when_input_is_negative():
    assert get_human_age(-10, -20) == [0, 0]


def test_return_one_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_return_two_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_return_three_human_years():
    assert get_human_age(28, 29) == [3, 3]


def test_with_large_numbers_input():
    assert get_human_age(100, 100) == [21, 17]
