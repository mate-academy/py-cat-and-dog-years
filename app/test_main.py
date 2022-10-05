from app.main import get_human_age


def test_params_zero_or_less():
    assert get_human_age(0, -1) == [0, 0]


def test_age_less_then_one_human_year():
    assert get_human_age(14, 14) == [0, 0]


def test_age_one_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_one_and_two_human_years():
    assert get_human_age(23, 23) == [1, 1]


def test_age_two_human_years():
    assert get_human_age(24, 24) == [2, 2]


def test_age_three_human_years():
    assert get_human_age(28, 29) == [3, 3]


def test_cat_older_then_dog():
    assert get_human_age(29, 15) == [3, 1]


def test_dog_older_then_cat():
    assert get_human_age(30, 15) == [3, 1]

