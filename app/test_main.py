from app.main import get_human_age


def test_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_if_younger_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_when_age_is_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_if_older_than_first_year_plus_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_when_age_is_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_check_difference() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_check_cat_and_dog_life_end_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
