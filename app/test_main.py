from app.main import get_human_age


def test_cats_and_dogs_age_is_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cats_and_dogs_age_is_between_15_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cats_and_dogs_age_is_above_24() -> None:
    assert get_human_age(100, 100) == [21, 17]
