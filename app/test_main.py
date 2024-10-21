from app.main import get_human_age


def test_return_zero_if_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_return_1_if_age_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_return_2_if_age_less_than_28() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_return_different_values_if_age_equals_28_and_more() -> None:
    assert get_human_age(28, 28) == [3, 2]
