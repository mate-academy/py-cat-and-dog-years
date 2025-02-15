from app.main import get_human_age


def test_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_human_age_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_human_age_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_human_age_varied() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_edge_cases() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(29, 29) == [3, 3]
    assert get_human_age(35, 35) == [4, 4]
