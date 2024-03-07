from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_over_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
