from app.main import get_human_age


def test_return_zeros_if_zeros_given() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_return_zeros_if_age_less_than_15() -> None:
    assert get_human_age(14, 9) == [0, 0]


def test_return_one_if_age_less_than_24() -> None:
    assert get_human_age(23, 15) == [1, 1]


def test_return_two_if_age_more_than_24() -> None:
    assert get_human_age(25, 27) == [2, 2]


def test_return_correct_value_for_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_return_correct_value_for_age_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
