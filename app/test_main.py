from app.main import get_human_age


def test_get_human_age_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_fourteen_years_is_zero_in_humans() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_fifteen_years_is_one_in_humans() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_fifteen_and_twenty_four() -> None:
    assert get_human_age(17, 20) == [1, 1]


def test_get_human_age_cat_age_after_twenty_four() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_dog_age_after_twenty_four() -> None:
    assert get_human_age(28, 29) == [3, 3]
