from app.main import get_human_age


def test_animal_age_is_negative_number() -> None:
    assert get_human_age(-100, -25) == [0, 0]


def test_animal_age_is_zero_or_less_then_one_human_year() -> None:
    assert get_human_age(0, 14) == [0, 0]


def test_animal_age_equal_to_one_human_year() -> None:
    assert get_human_age(23, 15) == [1, 1]


def test_animal_age_equal_to_two_human_years() -> None:
    assert get_human_age(24, 26) == [2, 2]


def test_different_rules_when_animal_age_more_then_two_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_different_rules_when_animal_age_really_large_numbers() -> None:
    assert get_human_age(99, 99) == [20, 17]
