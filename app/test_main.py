from app.main import get_human_age


def test_should_return_zero_when_value_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_value_negative() -> None:
    assert get_human_age(-184, -283) == [0, 0]


def test_correct_values_when_age_155_years() -> None:
    assert get_human_age(155, 155) == [34, 28]


def test_should_return_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_human_years_when_24() -> None:
    assert get_human_age(24, 24) == [2, 2]
