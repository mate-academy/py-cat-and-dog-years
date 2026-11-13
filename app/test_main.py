from app.main import get_human_age


def test_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_not_one_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_have_different_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_100_year() -> None:
    assert get_human_age(100, 100) == [21, 17]
