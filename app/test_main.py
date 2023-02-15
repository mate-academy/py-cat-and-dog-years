from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_is_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_is_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_is_29() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_get_human_age_is_101() -> None:
    assert get_human_age(101, 101) == [21, 17]
