from app.main import get_human_age

def test_should_return_zeros_when_the_ages_are_zeros():
    assert get_human_age(0, 0) == [0, 0]


def test_check_the_year_is_1_if_animals_year_is_15():
    assert get_human_age(15, 15) == [1, 1]


def test_check_if_the_year_is_0_if_the_age_is_under_15():
    assert get_human_age(14, 14) == [0, 0]


def test_check_the_year_is_1_if_the_age_is_under_24():
    assert get_human_age(23, 23) == [1, 1]


def test_check_the_year_is_2_if_animal_age_is_24():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_similar_age_to_27_year():
    assert get_human_age(27, 27) == [2, 2]


def test_cats_age_one_time_bigger_than_dogs_age():
    assert get_human_age(28, 28) == [3, 2]


def test_should_check_how_bigger_is_cats_life_than_dogs():
    assert get_human_age(100, 100) == [21, 17]
