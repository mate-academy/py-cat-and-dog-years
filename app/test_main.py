from app.main import get_human_age


def test_if_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_if_less_than_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_if_more_than_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_if_less_than_year_and_more_than_year() -> None:
    assert get_human_age(14, 15) == [0, 1]


def test_if_different_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
