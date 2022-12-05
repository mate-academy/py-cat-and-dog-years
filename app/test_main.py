from app.main import get_human_age


def test_animal_age_is_negative_number():
    assert get_human_age(-100, -25) == [0, 0]


def test_animal_age_is_zero_or_less_then_one_human_year():
    assert get_human_age(0, 14) == [0, 0]


def test_animal_age_equal_to_one_human_year():
    assert get_human_age(23, 15) == [1, 1]


def test_animal_age_equal_to_two_human_years():
    assert get_human_age(24, 26) == [2, 2]


def test_different_rules_for_cat_dog_when_animal_age_more_then_two_human_years():
    assert get_human_age(99, 99) == [20, 17]
