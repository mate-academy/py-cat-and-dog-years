from app.main import get_human_age


def test_zero_animals_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_zero_humans_ages():
    assert get_human_age(14, 14) == [0, 0]


def test_one_human_year_min_in_animals_ages():
    assert get_human_age(15, 15) == [1, 1]


def test_one_human_year_max_in_animals_ages():
    assert get_human_age(23, 23) == [1, 1]


def test_two_human_year_min_in_animals_ages():
    assert get_human_age(24, 24) == [2, 2]


def test_two_human_year_max_in_animals_ages():
    assert get_human_age(27, 27) == [2, 2]


def test_different_human_age():
    assert get_human_age(28, 28) == [3, 2]


def test_if_animal_age_is_big():
    assert get_human_age(100, 100) == [21, 17]
