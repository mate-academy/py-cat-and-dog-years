from app.main import get_human_age


def test_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_human_age_in_1_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_human_age_in_2_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_difference_between_cat_dog_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_human_age_in_3_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
