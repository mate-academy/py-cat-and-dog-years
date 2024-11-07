from app.main import get_human_age


def test_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_for_one_year_human() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_less_for_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_for_two_years_or_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_less_for_third_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_after_second_threshold_for_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_big_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
