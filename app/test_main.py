from app.main import get_human_age


def test_should_return_0_if_dogs_and_cats_age_less_than_15() -> None:
    assert get_human_age(12, 14) == [0, 0]


def test_counting_9_cats_and_dogs_years_as_1_human_year_after_15() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_counting_every_4_cats_years_as_1_human_year() -> None:
    assert get_human_age(44, 0) == [7, 0]


def test_counting_every_5_dogs_years_as_1_human_year_after_24() -> None:
    assert get_human_age(0, 39) == [0, 5]


def test_should_return_1_if_dogs_or_cats_age_is_equal_15() -> None:
    assert get_human_age(15, 0) == [1, 0]


def test_should_return_1_if_dogs_or_cats_age_is_23() -> None:
    assert get_human_age(23, 26) == [1, 2]


def test_should_return_21_and_17_if_dogs_and_cats_age_is_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
