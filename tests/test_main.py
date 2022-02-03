import random

from app.main import get_human_age


def test_should_return_zeros_if_both_ages_less_than_15():
    cat = random.randint(0, 14)
    dog = random.randint(0, 14)
    assert get_human_age(cat, dog) == [0, 0]


def test_should_return_ones_if_both_ages_from_15_to_23():
    cat = random.randint(15, 23)
    dog = random.randint(15, 23)
    assert get_human_age(cat, dog) == [1, 1]


def test_should_return_two_for_cat_if_age_from_24_to_27():
    cat = random.randint(24, 27)
    assert get_human_age(cat, 0)[0] == 2


def test_should_return_two_for_dog_if_age_from_24_to_28():
    dog = random.randint(24, 28)
    assert get_human_age(0, dog)[1] == 2


def test_should_return_result_for_cat_more_than_27_and_dog_more_than_28():
    assert get_human_age(100, 100) == [21, 17]
