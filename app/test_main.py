from app.main import get_human_age


def test_should_return_cat_and_dog_years():
    assert get_human_age(32, 29) == [4, 3]


def test_should_return_the_cat_is_older():
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_zero_when_less_years():
    assert get_human_age(10, 12) == [0, 0]


def test_should_return_one_year_in_15_to_24():
    assert get_human_age(17, 22) == [1, 1]
