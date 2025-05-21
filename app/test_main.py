from app.main import get_human_age


def test_should_return_zero_when_both_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_less_than_first_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_equal_to_first_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_ages_less_than_first_plus_second() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_equal_to_first_plus_second() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_ages_less_than_next_full_cycle() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_and_two_for_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_large_values_for_high_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
