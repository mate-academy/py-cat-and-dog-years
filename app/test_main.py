from app.main import get_human_age


def test_age_should_be_equal_to_zero_if_animal_age_less_then_15() -> None:
    assert get_human_age(14, 1) == [0, 0]


def test_age_should_be_equal_to_one_if_animal_age_less_then_24() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_age_should_be_equal_to_value_if_animal_age_above_24_is_divisible_by_each_year() -> None:
    assert get_human_age(32, 34) == [4, 4]


def test_age_should_be_whole_number_if_animal_age_above_24_not_divisible_by_each_year() -> None:
    assert get_human_age(33, 38) == [4, 4]


def test_age_should_be_zero_when_animal_age_is_a_negative_number() -> None:
    assert get_human_age(-4, -10) == [0, 0]
