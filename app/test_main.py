from app.main import get_human_age


def test_should_add_zeros_when_cat_and_dog_age_is_lower_15():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_cat_and_dog_age_equal_15():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_cat_and_dog_age_upper_15_and_lower_24():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_cat_and_dog_age_equal_24_and_lower_28():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_cat_and_dog_age_upper_24_and_lower_28():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_age_when_cat_and_dog_age_equal_28():
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_equal_human_age_when_cat_and_dog_age_is_different():
    assert get_human_age(28, 29) == [3, 3]


def test_should_return_age_when_cat_and_dog_age_equal_100():
    assert get_human_age(100, 100) == [21, 17]
