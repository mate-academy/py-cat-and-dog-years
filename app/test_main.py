from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_16_to_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_different_conversion_rates() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
