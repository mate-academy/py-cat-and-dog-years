from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_exactly_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_15_and_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_exactly_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_between_24_years_and_next_step() -> None:
    assert get_human_age(25, 27) == [2, 2]


def test_exactly_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_high_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_and_god_has_different_age() -> None:
    assert get_human_age(32, 20) == [4, 1]
