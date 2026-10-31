from app.main import get_human_age


def test_should_return_zero_when_both_ages_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_both_ages_are_between_15_and_23() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_should_return_two_when_both_ages_are_between_24_and_27() -> None:
    assert get_human_age(24, 27) == [2, 2]


def test_should_return_different_values_when_both_ages_are_equal_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_different_values_when_both_ages_are_equal_100() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_different_values_when_ages_are_different_1() -> None:
    assert get_human_age(15, 24) == [1, 2]


def test_should_return_different_values_when_ages_are_different_2() -> None:
    assert get_human_age(35, 40) == [4, 5]


def test_should_return_different_values_when_ages_are_different_3() -> None:
    assert get_human_age(0, 40) == [0, 5]
