from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_above_second_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_boundary_conditions() -> None:
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(0, 15) == [0, 1]
    assert get_human_age(24, 15) == [2, 1]
