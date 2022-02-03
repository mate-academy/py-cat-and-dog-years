from app.main import get_human_age


def test_should_return_zeroes_when_cat_and_dog_years_is_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeroes_when_cat_and_dog_years_is_less_then_14_years():
    assert get_human_age(14, 14) == [0, 0]


def test_when_age_of_both_animals_between_15_and_23_years():
    assert get_human_age(15, 23) == [1, 1]


def test_when_age_of_both_animals_between_24_and_27_years():
    assert get_human_age(24, 27) == [2, 2]


def test_when_cat_age_more_than_27_and_dog_age_more_than_28():
    assert get_human_age(100, 100) == [21, 17]
