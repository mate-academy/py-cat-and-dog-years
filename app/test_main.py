from app.main import get_human_age


def test_if_cat_or_dog_age_less_than_first_year():
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year_for_cat_and_dog():
    assert get_human_age(15, 15) == [1, 1]


def test_second_human_year_for_cat_and_dog():
    assert get_human_age(24, 24) == [2, 2]


def test_each_human_years_for_cat_and_dog():
    assert get_human_age(28, 29) == [3, 3]
