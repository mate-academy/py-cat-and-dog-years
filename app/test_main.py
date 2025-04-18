from app.main import get_human_age


def test_return_integers() -> None:
    assert get_human_age(31, 31) == [3, 3]


def test_when_values_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_return_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_return_2_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_return_3_human_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
