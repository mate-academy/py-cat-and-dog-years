from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_28_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_100_year() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_14_year() -> None:
    assert get_human_age(14, 14) == [0, 0]
