from app.main import get_human_age


def test_get_human_age_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_15_to_23() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_24_to_27() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_more_than_27() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
