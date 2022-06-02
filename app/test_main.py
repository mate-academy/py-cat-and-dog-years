from app.main import get_human_age


def test_cat_and_dog_ages_are_zeros():
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_ages_give_zero_human_age():
    assert get_human_age(10, 12) == [0, 0]


def test_cat_and_dog_ages_give_one_human_age():
    assert get_human_age(16, 23) == [1, 1]


def test_cat_and_dog_ages_give_two_human_age():
    assert get_human_age(16, 23) == [1, 1]


def test_the_same_cat_and_dog_age_give_different_human_age():
    assert get_human_age(28, 28) == [3, 2]


def test_big_value_of_cat_and_dog_ages():
    assert get_human_age(100, 100) == [21, 17]
