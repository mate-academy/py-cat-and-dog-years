from app.main import get_human_age

def test_if_age_both_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_convert_years_first() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_convert_years_second() -> None:
    assert  get_human_age(24, 24) == [2, 2]


def test_conver_more_then_two_years() -> None:
    assert  get_human_age(28,29) == [3, 3]
