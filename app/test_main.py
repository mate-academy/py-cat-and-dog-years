from app.main import get_human_age


def test_get_human_age_zero_ages() -> None:
    """Tests conversion of zero cat and dog ages."""
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_under_fifteen_cat_and_dog() -> None:
    """Tests conversion for cat and dog ages under 15."""
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_fifteen_cat_and_dog() -> None:
    """Tests conversion for cat and dog ages of 15."""
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_over_fifteen_but_under_twentyfour_cat() -> None:
    """Tests conversion for cat age between 15 and 24 (inclusive)."""
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_over_twentyfour_cat() -> None:
    """Tests conversion for cat age exceeding 24."""
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_cat_age() -> None:
    """Tests conversion for a larger cat age."""
    assert get_human_age(100, 100) == [21, 17]
