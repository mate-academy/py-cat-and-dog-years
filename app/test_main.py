from app.main import get_human_age


def test_zero_ages() -> None:
    # Test: both ages are 0 → result must be [0, 0]
    assert get_human_age(0, 0) == [0, 0]


def test_under_first_threshold() -> None:
    # Test: ages less than 15 → human age is 0
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_year() -> None:
    # Test: age 15 → first human year
    assert get_human_age(15, 15) == [1, 1]


def test_under_second_threshold() -> None:
    # Test: ages 16–23 → still 1 human year
    assert get_human_age(23, 23) == [1, 1]


def test_second_human_year() -> None:
    # Test: age 24 → second human year
    assert get_human_age(24, 24) == [2, 2]


def test_before_next_increase() -> None:
    # Test: age 27 → still 2 human years
    assert get_human_age(27, 27) == [2, 2]


def test_third_human_year_for_cat_only() -> None:
    # Test: age 28 → cat gets +1, dog does not
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    # Test: big ages → correct final values
    assert get_human_age(100, 100) == [21, 17]
