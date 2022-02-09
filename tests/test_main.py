from app.main import get_human_age


def test_first_fifteen_years_for_cat():
    assert get_human_age(15, 14) == [1, 0]


def test_first_fifteen_years_for_dog():
    assert get_human_age(14, 15) == [0, 1]


def test_boundary_years_for_pets():
    assert get_human_age(23, 23) == [1, 1]


def test_next_nine_years_for_pets():
    assert get_human_age(24, 24) == [2, 2]


def test_every_four_next_years_for_pets():
    assert get_human_age(28, 28) == [3, 2]


def test_every_five_next_years_for_pets():
    assert get_human_age(29, 29) == [3, 3]


def test_long_time_period_for_pets():
    assert get_human_age(100, 100) == [21, 17]
