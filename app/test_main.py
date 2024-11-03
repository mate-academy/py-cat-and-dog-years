from app.main import get_human_age


def test_zero_age_for_both() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_after_first_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_before_third_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_third_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
