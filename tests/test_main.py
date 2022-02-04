from app.main import get_human_age


def test_first_human_year():
    assert get_human_age(cat_age=0, dog_age=14) == [0, 0]


def test_second_human_year():
    assert get_human_age(cat_age=15, dog_age=23) == [1, 1]


def test_human_year_greater_2():
    assert get_human_age(cat_age=100, dog_age=100) == [21, 17]
