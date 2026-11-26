from app.main import get_human_age


def test_zero_years_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_14_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_first_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_next_9_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_next_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_every_next_year_for_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_next_29_years() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_different_years() -> None:
    assert get_human_age(10, 30) == [0, 3]
