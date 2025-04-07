from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 14) == [1, 0]
    assert get_human_age(14, 15) == [0, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 23) == [2, 1]
    assert get_human_age(23, 24) == [1, 2]


def test_additional_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(30, 35) == [3, 4]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
    assert get_human_age(1000, 1000) == [246, 197]


def test_asymmetric_inputs() -> None:
    assert get_human_age(40, 0) == [6, 0]
    assert get_human_age(0, 40) == [0, 5]
