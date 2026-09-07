from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_within_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_divergence() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_higher_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
