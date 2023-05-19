from app.main import get_human_age


def test_when_cat_and_dog_less_than_1_human_year() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_when_cat_and_dog_have_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_are_more_than_2_years_old() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
