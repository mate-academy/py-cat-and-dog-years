from app.main import get_human_age


def test_should_convert_into_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_convert_into_zero_when_age_less_zero() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_should_convert_into_1() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_convert_into_2() -> None:
    assert get_human_age(24, 24) == [2, 2]
