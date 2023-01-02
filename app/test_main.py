from app.main import get_human_age


def test_cat_age_and_dog_age_is_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_1_if_cat_age_and_dog_age_less_than_24():
    assert get_human_age(20, 20) == [1, 1]


def test_should_return_integer_if_cat_age_and_dog_age_more_than_24():
    assert get_human_age(28, 28) == [3, 2]
