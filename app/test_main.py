from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_before_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_before_next_cat_and_dog_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_gets_third_human_year_before_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_gets_third_human_year() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
