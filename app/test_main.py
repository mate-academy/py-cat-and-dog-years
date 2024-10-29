from app.main import get_human_age


def test_get_human_age_with_zero_years() -> None:
    """Test case for zero cat and dog years."""
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_with_cat_and_dog_below_threshold() -> None:
    """Test case for cat and dog ages below the threshold for human years."""
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_with_first_human_year() -> None:
    """Test case for ages equal to the first threshold for human years."""
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_with_ages_above_first_threshold() -> None:
    """Test case for cat and dog ages just above the first threshold."""
    assert get_human_age(16, 16) == [1, 1]


def test_get_human_age_with_second_human_year() -> None:
    """Test case for ages that should yield two human years."""
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_with_cat_years_exceeding_second_threshold() -> None:
    """Test case for cat ages exceeding the second threshold."""
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_with_large_ages() -> None:
    """Test case for large ages to verify calculations."""
    assert get_human_age(100, 100) == [21, 17]
