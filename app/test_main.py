from app.main import get_human_age


def test_cats_and_dogs_under_15_years() -> None:
    assert get_human_age(0, 5) == [0, 0]


def test_cats_and_dogs_in_15_to_23_years() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_cats_and_dogs_after_23_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cats_and_dogs_extra_year_after_23_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
