from app.main import get_human_age


def test_equal_to_zero_or_less():
    assert get_human_age(-5, 0) == [0, 0]


def test_one_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_less_then_one_human_year():
    assert get_human_age(14, 14) == [0, 0]


def test_less_then_two_human_years():
    assert get_human_age(23, 23) == [1, 1]


def test_equal_to_two_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_one_hundred_animal_years():
    assert get_human_age(100, 100) == [21, 17]


def test_five_hundred_animal_years():
    assert get_human_age(500, 500) == [121, 97]
