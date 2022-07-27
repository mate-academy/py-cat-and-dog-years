from app.main import get_human_age


def test_zero_human_age_when_animal_age_are_negative():
    assert get_human_age(-14, -1) == [0, 0]


def test_zero_human_age_when_animal_age_less_then_first_year():
    assert get_human_age(14, 0) == [0, 0]


def test_one_human_age_when_animal_age_less_then_second_year():
    assert get_human_age(23, 23) == [1, 1]


def test_two_human_age_when_animal_age_less_then_second_year_plus_each_yeah():
    assert get_human_age(27, 28) == [2, 2]


def test_three_human_age():
    assert get_human_age(28, 29) == [3, 3]


def test_large_human_age_when_animal_age_are_large():
    assert get_human_age(234, 456) == [54, 88]
