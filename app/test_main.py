from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_just_before_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_just_before_third_human_year_for_cats() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_exactly_third_human_year_for_cats() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_ages() -> None:
    assert get_human_age(29, 0) == [3, 0]
    assert get_human_age(32, 0) == [4, 0]
    assert get_human_age(33, 0) == [4, 0]
    assert get_human_age(44, 0) == [7, 0]


def test_dog_ages() -> None:
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 30) == [0, 3]
    assert get_human_age(0, 34) == [0, 4]
    assert get_human_age(0, 39) == [0, 5]
