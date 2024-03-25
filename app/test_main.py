from app.main import get_human_age


def test_all_numbers_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_14_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_24_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_first_28_year() -> None:
    assert get_human_age(25, 25) == [3, 2]
