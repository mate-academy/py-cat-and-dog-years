from app.main import get_human_age


def test_should_return_0_when_age_animal_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_when_age_animal_less_than_15():
    assert get_human_age(5, 14) == [0, 0]


def test_should_return_1_when_age_animal_from_15_to_23():
    assert get_human_age(15, 23) == [1, 1]


def test_should_return_2_when_age_is_24():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_3_when_age_is_28_and_29():
    assert get_human_age(28, 29) == [3, 3]


def test_every_next4_cat_and_next5_dog_years_give_1_extra_year():
    assert get_human_age(32, 44) == [4, 6]


def test_should_return_0_when_negative_values():
    assert get_human_age(-3, -14) == [0, 0]


def test_large_values():
    assert get_human_age(100, 100) == [21, 17]
