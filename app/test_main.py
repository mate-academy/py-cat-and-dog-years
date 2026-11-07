from app import main


def test_zero_ages_should_give_zero_human_years() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_below_first_threshold_should_give_zero() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_first_threshold_should_give_one_year() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_just_before_second_threshold_should_give_one_year() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_second_threshold_should_give_two_years() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_before_next_year_should_not_increment() -> None:
    assert main.get_human_age(27, 27) == [2, 2]


def test_cat_gets_extra_year_every_four_years() -> None:
    assert main.get_human_age(28, 0) == [3, 0]
    assert main.get_human_age(31, 0) == [3, 0]
    assert main.get_human_age(32, 0) == [4, 0]


def test_dog_gets_extra_year_every_five_years() -> None:
    assert main.get_human_age(0, 28) == [0, 2]
    assert main.get_human_age(0, 29) == [0, 3]
    assert main.get_human_age(0, 33) == [0, 3]
    assert main.get_human_age(0, 34) == [0, 4]


def test_large_ages() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_ages_are_independent() -> None:
    assert main.get_human_age(15, 0) == [1, 0]
    assert main.get_human_age(0, 15) == [0, 1]
    assert main.get_human_age(24, 15) == [2, 1]
