from app.main import get_human_age


def test_returns_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_young_age_returns_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_threshold_returns_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_threshold_returns_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_threshold_returns_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_reaches_third_threshold_before_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_reaches_third_threshold() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
