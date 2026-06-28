from app.main import get_human_age

# write your code here


def test_get_human_age_start() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_prev_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_prev_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_prev_third_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_third_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_old_year() -> None:
    assert get_human_age(100, 100) == [21, 17]
