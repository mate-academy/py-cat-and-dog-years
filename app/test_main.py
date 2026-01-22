from app.main import get_human_age


def test_get_cat_and_dog_age_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_cat_and_dog_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_cat_and_dog_age_no_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_cat_and_dog_age_sekond_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_cat_and_dog_age_third_year_zero() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_cat_and_dog_age_third_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_cat_and_dog_age_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
