from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_after_second_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
