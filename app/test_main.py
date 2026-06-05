from app.main import get_human_age


def test_if_animals_zero_years():
    age_animals = get_human_age(14, 14)
    assert age_animals == [0, 0]


def test_if_animals_one_years():
    age_animals = get_human_age(15, 15)
    assert age_animals == [1, 1]


def test_if_animals_two_years():
    age_animals = get_human_age(24, 24)
    assert age_animals == [2, 2]


def test_if_animals_three_years():
    age_animals = get_human_age(28, 29)
    assert age_animals == [3, 3]


def test_if_animals_up_2_years():
    age_animals = get_human_age(23, 23)
    assert age_animals == [1, 1]


def test_if_animals_more_years():
    age_animals = get_human_age(100, 100)
    assert age_animals == [21, 17]