from app.main import get_human_age


def test_zero_ages_of_animals():
    assert get_human_age(14, 14) == [0, 0]


def test_first_ages_of_animals():
    assert get_human_age(15, 15) == [1, 1]


def test_second_ages_of_animals():
    assert get_human_age(24, 24) == [2, 2]


def test_different_age_of_the_animal():
    assert get_human_age(28, 29) == [3, 3]
