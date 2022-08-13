from app.main import get_human_age


def test_return_zero_when_year_less_15():
    assert get_human_age(14, 14) == [0, 0]


def test_plus_one_next_9_year():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_add_extra_1_year_each_4_years():
    assert get_human_age(28, 28) == [3, 2]


def test_dog_add_extra_1_year_each_5_years():
    assert get_human_age(27, 29) == [2, 3]


def test_when_age_equal_negative():
    assert get_human_age(-1, -2) == [0, 0]


def test_when_age_equal_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_when_age_large_numbers():
    assert get_human_age(100, 100) == [21, 17]
