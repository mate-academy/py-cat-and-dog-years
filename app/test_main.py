from app.main import get_human_age


def test_should_return_zero_year_after_birthday() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_one_year_after_first_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_years_after_first_24_years() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_cat_should_get_extra_year_every_4_years() -> None:
    assert get_human_age(27, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]


def test_dog_should_get_extra_year_every_5_years() -> None:
    assert get_human_age(0, 28) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]


def test_should_add_years_for_older_pets() -> None:
    assert get_human_age(32, 34) == [4, 4]
