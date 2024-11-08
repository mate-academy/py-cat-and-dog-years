from app.main import get_human_age


def test_get_cat_age_and_dog_age_equal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_cat_age_and_dog_age_equal_zero2() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_cat_age_and_dog_age_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_cat_age_and_dog_age_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_cat_age_and_dog_age_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_cat_age_and_dog_age_third() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_cat_age_and_dog_age_equal_different() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_cat_age_and_dog_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
