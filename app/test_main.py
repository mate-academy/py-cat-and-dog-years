from app.main import get_human_age


def test_should_check_when_values_are_incomplete() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_check_when_values_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_check_when_values_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_check_when_values_not_two_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_check_when_values_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_check_when_values_not_three_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_check_when_values_three_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_check_when_values_one_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
