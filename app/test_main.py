from app.main import get_human_age


def test_first_15_cat_or_dog_years_give_1_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_the_next_9_cat_or_dog_years_give_1_more_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_every_4_next_cat_years_give_1_extra_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_every_5_next_dog_years_give_1_extra_human_year() -> None:
    assert get_human_age(100, 100) == [21, 17]
