from app.main import get_human_age

def test_should_return_zero_when_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_age_is_less_then_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_is_equal_greater_15() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_age_is_equal_greater_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_three_for_cat_when_age_is_equal_greater_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_different_value_for_cat_and_dog() -> None:
    assert get_human_age(100, 100) == [21, 17]
