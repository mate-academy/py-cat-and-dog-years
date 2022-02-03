from random import randint


from app.main import get_human_age


def test_first_human_year():
    cat_years = randint(0, 14)
    dog_years = randint(0, 14)

    assert get_human_age(cat_years, dog_years) == [0, 0]


def test_second_human_year():
    cat_years = randint(15, 23)
    dog_years = randint(15, 23)

    assert get_human_age(cat_years, dog_years) == [1, 1]


def test_human_year_greater_2():
    assert get_human_age(100, 100) == [21, 17]
