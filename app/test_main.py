from app.main import get_human_age


def test_when_zeros_are_given() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_15_equals_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_24_equals_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_28_equals_3_and_2() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_29_equals_3() -> None:
    assert get_human_age(29, 29) == [3, 3]
