from app.main import get_human_age


def when_age_equals_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_next_9_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_extra_human_year_cat() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_extra_human_year_dog() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_extra_human_year_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_input() -> None:
    assert get_human_age(100, 100) == [21, 17]
