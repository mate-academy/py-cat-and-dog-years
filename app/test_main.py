from app.main import get_human_age


def test_not_years_for_animals():
    assert get_human_age(0, 0) == [0, 0]


def test_so_small_years_for_animals():
    assert get_human_age(14, 14) == [0, 0]


def test_one_years_for_animals():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_two_years_for_animals():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_yeas_separately_for_cat_and_dog():
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
