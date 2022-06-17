from app.main import get_human_age


def test_check_if_animal_age_is_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_check_if_animal_age_is_one():
    assert get_human_age(15, 15) == [1, 1]


def test_check_if_animal_age_is_one_next():
    assert get_human_age(23, 23) == [1, 1]


def test_check_if_animal_age_is_two():
    assert get_human_age(27, 27) == [2, 2]


def test_check_when_dog_and_cat_have_different_age():
    assert get_human_age(28, 28) == [3, 2]


def test_check_when_dog_and_cat_have_one_hundred_age():
    assert get_human_age(100, 100) == [21, 17]
