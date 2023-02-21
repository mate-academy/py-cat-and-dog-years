from app.main import get_human_age


def test_returns_list() -> None:
    assert type(get_human_age(1, 1)) is list


def test_not_positive_years() -> None:
    assert get_human_age(-1, 0) == [0, 0]


def test_0_human_year() -> None:
    assert get_human_age(13, 14) == [0, 0]


def test_1_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_2_human_years() -> None:
    assert get_human_age(24, 25) == [2, 2]


def test_more_human_years() -> None:
    assert get_human_age(29, 35) == [3, 4]
