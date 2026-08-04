from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_threshold_returns_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_threshold_returns_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshold_still_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_threshold_plus_one_returns_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_extra_years_dog_not() -> None:
    assert get_human_age(28, 27) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_different_progressions() -> None:
    # Cat 30 years: 15 -> 1, 9 -> +1, (30-24)//4=1 -> +1 => 3
    # Dog 30 years: 15 -> 1, 9 -> +1, (30-24)//5=1 -> +1 => 3
    assert get_human_age(30, 30) == [3, 3]
