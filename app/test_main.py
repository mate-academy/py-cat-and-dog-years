from app.main import get_human_age


def test_both_ages_equal_to_0():
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_human_year():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_different_values_for_same_age():
    assert get_human_age(28, 28) == [3, 2]


def test_first_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_big_ages():
    assert get_human_age(100, 100) == [21, 17]
