from app.main import get_human_age


def test_should_return_zeros_when_ages_equals_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_when_ages_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_ages_equals_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_when_ages_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_when_ages_greater_than_24() -> None:
    assert get_human_age(24, 24) == [2, 2]
