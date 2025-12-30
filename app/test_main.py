from app.main import get_human_age


def test_zero_human_age_when_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_zero_human_age_when_less_than_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_two_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_big_human_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
