from app.main import get_human_age


def test_should_return_zero_when_both_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_both_under_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_both_are_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_still_be_one_when_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_still_be_two_when_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_for_cat_and_two_for_dog_when_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_for_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
