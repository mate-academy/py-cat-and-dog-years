from app.main import get_human_age


def test_zeros_when_age_lover_than_fourteen():
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_when_age_is_fifteen():
    assert get_human_age(15, 15) == [1, 1]


def test_returns_one_when_age_is_bigger_than_15_and_lower_than_24():
    assert get_human_age(23, 23) == [1, 1]


def test_func_return_2_when_age_is_24():
    assert get_human_age(24, 24) == [2, 2]


def test_returns_2_when_upper_24_and_lower_28():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_different_values_when_age_is_28():
    assert get_human_age(28, 28) == [3, 2]


def test_for_age_is_29():
    assert get_human_age(29, 29) == [3, 3]


def test_return_different_values_when_age_is_above_28():
    assert get_human_age(35, 35) == [4, 4]


def test_returns_21_and_17_when_age_is_100():
    assert get_human_age(100, 100) == [21, 17]
