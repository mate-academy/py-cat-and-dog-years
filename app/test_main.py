from app.main import get_human_age


def test_cat_dog_years_less_than_first_years() -> None:
    assert get_human_age(10, 10) == [0, 0]


def test_cat_dog_years_equals_first_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_dog_years_more_than_first_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
