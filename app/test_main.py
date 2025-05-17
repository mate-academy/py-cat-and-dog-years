from app.main import get_human_age


def test_zero_ages_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_first_threshold_should_return_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_at_first_threshold_should_return_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold_should_return_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_at_second_threshold_should_return_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_above_second_threshold_returns_two() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_one_unit_above_second_threshold_should_increase_cat_only() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_high_values_should_match_expected_conversion() -> None:
    assert get_human_age(100, 100) == [
        21, 17
    ]
