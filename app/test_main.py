from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_bellow_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_second_year_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_more_years() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_age_between_first_second() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_between_second_third() -> None:
    assert get_human_age(27, 27) == [2, 2]
