from app.main import get_human_age


def test_should_return_human_age_is_equal_zero():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_human_age_is_equal_one():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_human_age_is_equal_two():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_human_age_when_cat_age_and_dog_age_are_equals_28():
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_human_age_when_cat_age_and_dog_age_reach_100():
    assert get_human_age(100, 100) == [21, 17]
