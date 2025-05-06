from app.main import get_human_age


def test_at_least_0_years_ago() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_15_years_old() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_minimum_value_for_animals() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_average_value_of_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_maximum_value_for_animals() -> None:
    assert get_human_age(100, 100) == [21, 17]
