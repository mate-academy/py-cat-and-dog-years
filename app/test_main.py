from app.main import get_human_age


def test_should_return_zeros_if_animals_ages_are_zeros():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_if_animals_ages_less_15():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_ones_if_animals_ages_are_15():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_ones_if_animals_ages_are_less_24():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_twos_if_animals_ages_are_24():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_twos_if_animals_ages_are_more_24():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_for_cat_if_cat_age_is_28():
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_three_for_dog_if_dog_age_is_29():
    assert get_human_age(28, 29) == [3, 3]


def test_should_count_correctly_if_animals_ages_are_more_29():
    assert get_human_age(100, 100) == [21, 17]
