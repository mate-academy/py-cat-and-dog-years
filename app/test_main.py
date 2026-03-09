from app.main import get_human_age


def test_returns_zero_if_age_is_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_returns_1_if_age_is_between_15_and_23() -> None:
    assert get_human_age(15, 23) == [1, 1]

def test_returns_2_if_age_more_23() -> None:
    assert get_human_age(27, 28) == [2, 2]

def test_returns_3_and_more() -> None:
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(37, 35) == [5, 4]
    assert get_human_age(56, 40) == [10, 5]