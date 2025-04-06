from app.main import get_human_age



def test_returns_zeroes_for_zero_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_returns_zeroes_for_ages_below_15():
    assert get_human_age(14, 14) == [0, 0]


def test_returns_ones_for_ages_between_15_and_24():
    assert get_human_age(23, 23) == [1, 1]


def test_calculates_next_years_correctly():
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_returns_correct_human_age_for_100():
    assert get_human_age(100, 100) == [21, 17]
