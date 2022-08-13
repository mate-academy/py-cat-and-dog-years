from app.main import get_human_age


def test_should_return_zero_when_ages_less_15():
    assert get_human_age(0, 14) == [0, 0]


def test_should_return_1_when_ages_between_15_and_23():
    assert get_human_age(15, 23) == [1, 1]


def test_should_add_1_year_every_4_pets_years_when_ages_24_and_more():
    assert get_human_age(100, 28) == [21, 2]


def test_should_return_zero_when_age_equal_0():
    assert get_human_age(-3, -1) == [0, 0]
