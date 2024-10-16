from app.main import get_human_age


def test_zero_age() -> None:
    """Test when both cat and dog are 0 years old"""
    assert get_human_age(0, 0) == [0, 0]


def test_cat_age_less_than_15_dog_age_less_than_15() -> None:
    """Test when both cat and dog ages
    are less than 15 (no human year equivalent)"""
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_exactly_15_years() -> None:
    """Test when both cat and dog
    are exactly 15 years old (first human year)"""
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_age_23_years() -> None:
    """Test when both cat and dog are 23 years old (still first human year)"""
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_exactly_24_years() -> None:
    """Test when both cat and dog are 24 years old (second human year)"""
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_age_27_years() -> None:
    """Test when both cat and dog are 27 years old (still second human year)"""
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_age_28_years() -> None:
    """Test when both cat and dog
    are 28 years old (cat: 3 human years, dog: still 2)"""
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages_100_years() -> None:
    """Test when both cat and dog are 100 years old (human years are higher)"""
    assert get_human_age(100, 100) == [21, 17]
