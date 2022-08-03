from app.main import get_human_age


def test_cat_dog_age_zero_year():
    ages = get_human_age(14, 14)
    assert ages == [0, 0]


def test_cat_dog_age_exactly_one_year():
    ages = get_human_age(15, 15)
    assert ages == [1, 1]


def test_cat_dog_age_still_one_year():
    ages = get_human_age(23, 23)
    assert ages == [1, 1]


def test_cat_dog_age_exactly_two_years():
    ages = get_human_age(24, 24)
    assert ages == [2, 2]


def test_cat_dog_age_still_two_years():
    ages = get_human_age(26, 26)
    assert ages == [2, 2]


def test_cat_age_more_than_two_years():
    ages = get_human_age(28, 28)
    assert ages == [3, 2]


def test_cat_dog_age_random_years():
    ages = get_human_age(100, 100)
    assert ages == [21, 17]