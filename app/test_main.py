from app.main import get_human_age


def test_cat_and_dog_have_age_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_expected_value():
    assert get_human_age(23, 23) == [1, 1]


def test_high_ages():
    assert get_human_age(100, 100) == [21, 17]


def test_dog_is_older_than_cat():
    assert get_human_age(14, 28) == [0, 2]


def test_cat_is_older_than_dog():
    assert get_human_age(28, 14) == [3, 0]


def test_cat_and_dog_should_return_different_result():
    assert get_human_age(28, 28) == [3, 2]
