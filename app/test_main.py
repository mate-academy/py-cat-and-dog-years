from app.main import get_human_age


def if_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def if_ages_are_both_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def if_ages_are_both_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def if_ages_are_both_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def if_ages_are_both_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def if_ages_are_both_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def if_ages_are_both_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def if_ages_are_both_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
