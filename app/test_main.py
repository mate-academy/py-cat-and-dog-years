from app.main import get_human_age


def test_less_than_one_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_extra_human_years_for_cats() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_extra_human_years_for_all_animals() -> None:
    assert get_human_age(100, 100) == [21, 17]
