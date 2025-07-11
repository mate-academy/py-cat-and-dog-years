from app.main import get_human_age


def test_get_human_age_if_zeros_was_given() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_first_year_end() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_second_year_start() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_year_end() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_different_each_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_if_hundreds() -> None:
    assert get_human_age(100, 100) == [21, 17]
