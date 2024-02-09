from app.main import get_human_age


def test_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0], "Age 0 should return [0, 0]"


def test_age_before_first_porig() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_first_year_limit() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_second() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_second_porig() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_age_third() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17], "Higher ages return [21, 17]"
