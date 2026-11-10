from app.main import get_human_age


def test_zero_ages_should_return_zeroes() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_less_than_fifteen_should_return_zeroes() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_fifteen_ages_should_return_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_less_than_twenty_four_should_return_one_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_twenty_four_ages_should_return_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_twenty_seven_ages_boundary() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_twenty_eight_ages_boundary_cat_gets_extra_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages_conversion() -> None:
    assert get_human_age(100, 100) == [21, 17]
