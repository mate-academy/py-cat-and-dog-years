from app.main import get_human_age


def test_animal_age_equal_to_zero():
    assert get_human_age(0, 100) == [0, 17]

    assert get_human_age(100, 0) == [21, 0]


def test_is_equal_to_human_one():
    assert get_human_age(15, 15) == [1, 1]

    assert get_human_age(23, 23) == [1, 1]


def test_is_equal_to_human_two():

    assert get_human_age(24, 24) == [2, 2]

    assert get_human_age(27, 27) == [2, 2]


def test_equal_animals_ages_different_human_ages():

    assert get_human_age(28, 28) == [3, 2]
