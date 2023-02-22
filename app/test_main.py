from app.main import get_human_age


def test_zero_years_in_both() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_fifteen_years_in_cat() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_23_years_in_both() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_years_in_both() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_27_years_in_both() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_28_years_in_both() -> None:
    assert get_human_age(28, 28) == [3, 2]

