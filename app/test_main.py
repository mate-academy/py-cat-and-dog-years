from app.main import get_human_age

def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_lower_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_equal_to_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_first_and_second_year() -> None:
    assert get_human_age(20, 20) == [1, 1]


def test_age_equal_to_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_between_second_and_third_year() -> None:
    assert get_human_age(26, 26) == [2, 2]


def test_age_equal_to_third_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_more_then_ten_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
