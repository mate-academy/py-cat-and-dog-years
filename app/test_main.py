from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_negative_ages() -> None:
    assert get_human_age(-1, -2) == [0, 0]


def test_age_less_than_first_year() -> None:
    assert get_human_age(11, 12) == [0, 0]


def test_age_equals_or_more_than_first_year() -> None:
    assert get_human_age(15, 17) == [1, 1]


def test_age_equals_or_more_than_second_year() -> None:
    assert get_human_age(26, 24) == [2, 2]


def test_age_equals_or_more_than_third_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_work_with_greater_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
