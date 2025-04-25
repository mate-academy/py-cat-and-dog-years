from app.main import get_human_age


def test_get_human_age_cat_and_dog_young() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_cat_and_dog_just_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_cat_and_dog_still_one_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_cat_and_dog_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_cat_extra_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_get_human_age_dog_extra_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
