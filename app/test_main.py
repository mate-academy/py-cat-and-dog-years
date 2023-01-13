from app.main import get_human_age


def test_should_return_zero_when_age_is_zero_or_negative() -> None:
    assert get_human_age(-1, 0) == [0, 0]


def test_should_return_zero_when_age_is_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_age_is_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_correct_value_when_age_is_less_than_29() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_value_when_age_is_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
