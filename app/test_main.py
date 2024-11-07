from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_three_years() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_get_human_age_large() -> None:
    assert get_human_age(44, 49) == [7, 7]


def test_get_human_age_boundary_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_boundary_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_only_int() -> None:
    res = get_human_age(10, 10)
    assert isinstance(res[0] and res[1], int) is True
