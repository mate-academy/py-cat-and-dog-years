from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_third_human_year_cat_extra() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_additional_boundary_cases() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(32, 34) == [4, 4]
    assert get_human_age(34, 29) == [3, 3]
