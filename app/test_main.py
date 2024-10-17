from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_third_year_cat() -> None:
    assert get_human_age(28, 0) == [3, 0]


def test_get_human_age_third_year_dog() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_get_human_age_multiple_years() -> None:
    assert get_human_age(44, 49) == [7, 7]


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
