from app.main import get_human_age

def test_returns_zero_for_zero_input():
    assert get_human_age(0, 0) == [0, 0]


def test_returns_zero_for_ages_below_first_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_for_exact_first_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_returns_one_for_ages_between_first_and_second_thresholds():
    assert get_human_age(23,23) == [1, 1]


def test_returns_two_for_exact_second_threshold():
    assert get_human_age(24, 24) == [2, 2]


def test_returns_two_for_ages_just_below_next_conversion_step():
    assert get_human_age(27, 27) == [2, 2]


def test_returns_correct_values_when_one_age_passes_extra_threshold():
    assert get_human_age(28, 28) == [3, 2]


def test_returns_correct_values_for_large_ages():
    assert get_human_age(100, 100) == [21, 17]
