from app.main import get_human_age


def test_should_return_zeros_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_at_fourteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_ones_at_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_ones_at_twenty_three_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_twos_at_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_twos_at_twenty_seven_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_give_cat_third_year_at_28_while_dog_has_two() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_give_dog_third_year_at_29() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_give_cat_fourth_year_at_32() -> None:
    assert get_human_age(32, 32) == [4, 3]


def test_should_not_mix_up_cat_and_dog_ages() -> None:
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(0, 15) == [0, 1]


def test_should_convert_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
