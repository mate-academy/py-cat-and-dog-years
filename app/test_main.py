from app.main import get_human_age


def test_ages_less_than_fifteen():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_ages_for_one_human_year():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_ages_for_two_human_years():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_different_ages_for_older_animals():
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
