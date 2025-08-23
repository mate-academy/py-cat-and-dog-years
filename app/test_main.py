
from app.main import get_human_age  # Adjust import if needed


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_human_year() -> None:
    # 14 cat/dog years should still be 0 human years
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_human_year() -> None:
    # 15 cat/dog years => 1 human year
    assert get_human_age(15, 15) == [1, 1]


def test_after_first_human_year() -> None:
    # 23 cat/dog years still 1 human year
    assert get_human_age(23, 23) == [1, 1]


def test_start_second_human_year() -> None:
    # 24 cat/dog years start second human year
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_cat_years() -> None:
    # Cat years: 27 still 2 human years (24-27)
    assert get_human_age(27, 27) == [2, 2]


def test_third_cat_years_and_second_dog_year() -> None:
    # Cat: 28 => 3 human years, Dog: 28 => 2 human years
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    # Large ages, cat and dog
    assert get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_different_ages() -> None:
    # Different ages edge case
    assert get_human_age(15, 24) == [1, 2]
    assert get_human_age(23, 29) == [1, 2]
    assert get_human_age(30, 50) == [3, 5]
