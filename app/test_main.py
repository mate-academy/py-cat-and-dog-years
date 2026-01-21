from app.main import get_human_age


def test_less_than_15() -> None:
    assert (get_human_age(0, 0) == [0, 0])


def test_equal_15() -> None:
    assert (get_human_age(15, 15) == [1, 1])


def test_next_9() -> None:
    assert (get_human_age(24, 24) == [2, 2])


def test_next_5() -> None:
    assert (get_human_age(28, 28) == [3, 2])


def test_big_age() -> None:
    assert (get_human_age(100, 100) == [21, 17])
