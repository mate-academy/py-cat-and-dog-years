from app.main import get_human_age


def test_get_human_age_zeros():
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_below_second_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_threshold():
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_above_second_threshold():
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_extra_years_cat():
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_boundary():
    assert get_human_age(100, 100) == [21, 17]
