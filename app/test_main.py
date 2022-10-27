

from app.main import get_human_age


def test_should_return_zeros_when_input_is_negative() -> None:
    assert get_human_age(-13, -2) == [0, 0]


def test_should_return_zeros_when_input_less_than_15() -> None:
    assert get_human_age(10, 10) == [0, 0]


def test_should_return_1_when_input_less_than_24() -> None:
    assert get_human_age(16, 18) == [1, 1]


def test_should_return_expected_value_when_input_more_than_24() -> None:
    assert get_human_age(26, 27) == [2, 2]
