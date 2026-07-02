from app import main


def test_should_return_zeros_for_ages_less_than_fifteen() -> None:
    assert main.get_human_age(14, 14) == [0, 0]
    assert main.get_human_age(0, 0) == [0, 0]


def test_should_return_one_human_year_at_exactly_fifteen_years() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_stay_one_human_year_just_before_twenty_four() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_human_years_at_exactly_twenty_four() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_stay_two_human_years_just_before_next_step() -> None:
    assert main.get_human_age(27, 28) == [2, 2]


def test_should_increment_cat_age_every_four_years_after_twenty_four() -> None:
    assert main.get_human_age(28, 24) == [3, 2]
    assert main.get_human_age(31, 24) == [3, 2]
    assert main.get_human_age(32, 24) == [4, 2]


def test_should_increment_dog_age_every_five_years_after_twenty_four() -> None:
    assert main.get_human_age(24, 29) == [2, 3]
    assert main.get_human_age(24, 33) == [2, 3]
    assert main.get_human_age(24, 34) == [2, 4]
