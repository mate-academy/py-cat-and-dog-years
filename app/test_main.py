from app.main import get_human_age


def test_if_incoming_data_is_0():
    assert get_human_age(0, 0) == [0, 0]


def test_if_incoming_years_is_less_or_equal_15():
    assert get_human_age(15, 10) == [1, 0]


def test_if_incoming_years_is_less_or_equal_24():
    assert get_human_age(24, 20) == [2, 1]


def test_if_incoming_years_is_less_or_equal_28():
    assert get_human_age(28, 28) == [3, 2]


def test_if_incoming_years_is_more_than_28():
    assert get_human_age(100, 100) == [21, 17]
