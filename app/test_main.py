from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_first_15_years_boundary() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_9_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_second_9_years_boundary() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_extra_4_years_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_extra_4_years_cat_boundary() -> None:
    assert get_human_age(100, 100) == [21, 17]
