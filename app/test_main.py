from app.main import get_human_age


def test_if_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_first_period() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_must_be_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_second_period() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_must_be_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_third_period() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_age_must_be_3() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_if_age_is_huge_value() -> None:
    assert get_human_age(98, 99) == [20, 17]
