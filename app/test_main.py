from app.main import get_human_age


def test_zero_ages_should_return_zero_human_years() -> None:
    """Test that zero cat and dog ages return zero human years."""
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_first_threshold_should_return_zero_human_years() -> None:
    """Test that a below the first threshold return 0 human y."""
    assert get_human_age(14, 14) == [0, 0]


def test_age_equal_to_first_threshold_should_return_one_human_year() -> None:
    """Test that a equal to the 1st threshold return one y."""
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_first_and_second_threshold_should_return_one_human_year() -> None:
    """Test that a between the 1 and 2 threshold return 1 y."""
    assert get_human_age(23, 23) == [1, 1]


def test_age_equal_to_second_threshold_should_return_two_human_years() -> None:
    """Test that a = to the 2 threshold return 2 human y."""
    assert get_human_age(24, 24) == [2, 2]


def test_age_between_second_threshold_and_next_conversion_should_return_two_human_years() -> None:
    """Test that a between the 2 threshold and the next 2 y."""
    assert get_human_age(27, 27) == [2, 2]


def test_age_past_second_threshold_should_calculate_extra_years_correctly() -> None:
    """Test that a past the 2 threshold calc ext human y correct."""
    assert get_human_age(28, 28) == [3, 2]


def test_large_age_values_should_return_correct_human_years() -> None:
    """Test that large age values return correct human years."""
    assert get_human_age(100, 100) == [21, 17]
    assert get_human_age(200, 200) == [46, 37]
