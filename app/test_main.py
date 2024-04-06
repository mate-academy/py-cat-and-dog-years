from app.main import get_human_age


def test_for_get_human_age_if_years_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_for_get_human_age_if_years_less_than_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_for_get_human_age_if_years_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_for_get_human_age_if_years_less_than_twenty_four() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_for_get_human_age_if_years_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_for_get_human_age_if_years_less_than_twenty_eight() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_for_get_human_age_if_years_twenty_eight() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_for_get_human_age_if_years_more_than_twenty_eight() -> None:
    assert get_human_age(100, 100) == [21, 17]
