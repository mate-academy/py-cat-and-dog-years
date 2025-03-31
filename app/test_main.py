from app.main import get_human_age


def test_should_return_zero_when_ages_less_15():
    assert get_human_age(0, 14) == [0, 0]


def test_should_return_1_when_ages_15_and_23():
    assert get_human_age(15, 23) == [1, 1]


def test_should_return_2_when_ages_cat_24_to_27_and_dog_to_28():
    assert get_human_age(27, 28) == [2, 2]


def test_should_add_1_year_every_4_pets_years_when_ages_from_28():
    assert get_human_age(28, 100) == [3, 17]


def test_should_return_zero_when_age_incorrect():
    assert get_human_age(-3, -1) == [0, 0]
