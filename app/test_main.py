from app.main import get_human_age


def test_cat_dog_age_zero_year():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_dog_age_exactly_one_year():
    assert get_human_age(15, 15) == [1, 1]


def test_cat_dog_age_still_one_year():
    assert get_human_age(23, 23) == [1, 1]


def test_cat_dog_age_exactly_two_years():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_age_still_two_years():
    assert get_human_age(26, 26) == [2, 2]


def test_cat_age_more_than_two_years():
    assert get_human_age(28, 28) == [3, 2]


def test_cat_dog_age_random_years():
    assert get_human_age(100, 100) == [21, 17]
