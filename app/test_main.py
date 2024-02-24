from app.main import get_human_age


def test_dog_and_cat_years_should_convert_into_1_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_dog_and_cat_years_should_convert_into_1_more_human_year() -> None:
    assert get_human_age(24, 23) == [2, 1]


def test_dog_years_should_convert_into_1_extra_human_year() -> None:
    assert get_human_age(28, 29) == [3, 3]
