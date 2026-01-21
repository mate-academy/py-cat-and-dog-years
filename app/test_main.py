from app.main import get_human_age


def test_if_animal_age_is_less_than_15_should_return_0():
    assert get_human_age(0, 14) == [0, 0]


def test_if_animal_age_is_between_15_and_23_should_return_1():
    assert get_human_age(16, 23) == [1, 1]


def test_age_is_bigger_than_23_should_return_result_is_more_than_1():
    assert get_human_age(24, 29) == [2, 3]


def test_if_cat_age_is_more_than_23_every_4_next_years_give_1():
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(78, 0) == [15, 0]


def test_if_dog_age_is_more_than_23_every_5_next_years_give_1():
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(0, 78) == [0, 12]


def test_human_age_is_int():
    human_age = get_human_age(1, 99)
    assert isinstance(human_age[0], int) \
           and isinstance(human_age[1], int) is True
