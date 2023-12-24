from app.main import get_human_age


def test_if_age_is_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_if_age_is_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_if_age_is_more_than_15():
    assert get_human_age(23, 23) == [1, 1]


def test_if_age_is_more_than_24():
    assert get_human_age(27, 27) == [2, 2]


def test_if_age_is_very_old():
    assert get_human_age(100, 100) == [21, 17]
