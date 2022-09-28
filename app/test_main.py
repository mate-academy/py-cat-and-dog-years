from app.main import get_human_age


def test_zero_ages():
    assert get_human_age(16, 14) == [1, 0]


def test_first_ages():
    assert get_human_age(24, 24) == [2, 2]


def test_second_ages():
    assert get_human_age(28, 28) == [3, 2]


def test_third_ages():
    assert get_human_age(100, 100) == [21, 17]
