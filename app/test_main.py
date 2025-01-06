from app.main import get_human_age


def check_get_human() -> None:
    assert (get_human_age(0, 0) == [0, 0])


def check_middle_age() -> None:
    assert (get_human_age(14, 14) == [0, 0])


def check_next_age_gap() -> None:
    assert (get_human_age(15, 15) == [1, 1])


def check_next_age_gap1() -> None:
    assert (get_human_age(23, 23) == [1, 1])


def check_next_age_gap2() -> None:
    assert (get_human_age(24, 24) == [2, 2])


def check_next_age_gap3() -> None:
    assert (get_human_age(27, 27) == [2, 2])


def check_next_age_gap4() -> None:
    assert (get_human_age(28, 28) == [3, 2])


def check_last_age_gap() -> None:
    assert (get_human_age(100, 100) == [21, 17])
