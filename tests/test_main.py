from random import randint


from app.main import get_human_age


def test_first_human_year():
    cat_years = 14
    dog_years = 7

    assert get_human_age(cat_years, dog_years) == [0, 0]


def test_second_human_year():
    cat_years = 15
    dog_years = 23

    assert get_human_age(cat_years, dog_years) == [1, 1]


def test_human_year_greater_2():
    assert get_human_age(100, 100) == [21, 17]
