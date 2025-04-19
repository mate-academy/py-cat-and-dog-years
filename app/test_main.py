from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_under_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_almost_next_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_next_human_year_for_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
