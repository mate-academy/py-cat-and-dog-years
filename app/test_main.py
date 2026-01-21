from app.main import get_human_age


def test_dogs_and_cats_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_humans_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_humans_twenty_three_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_humans_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_humans_twenty_seven_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_humans_twenty_eight_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_humans_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
