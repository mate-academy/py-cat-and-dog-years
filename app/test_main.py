from app.main import get_human_age


def test_should_return_zero_if_age_equal_to_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_if_age_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_year_if_age_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_if_age_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_three_for_cat_and_two_for_dog_for_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_value_for_age_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
