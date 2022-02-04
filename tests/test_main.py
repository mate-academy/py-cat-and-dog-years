from app.main import get_human_age


def test_first_human_year():
    assert get_human_age(cat_years=0, dog_years=14) == [0, 0]


def test_second_human_year():
    assert get_human_age(cat_years=15, dog_years=23) == [1, 1]


def test_human_year_greater_2():
    assert get_human_age(100, 100) == [21, 17]
