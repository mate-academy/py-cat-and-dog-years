from app.main import get_human_age


def test_first_fifteen_cat_years_should_give_one_human_year() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_next_nine_cat_years_should_give_one_more_human_year() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_every_four_next_cat_years_should_give_one_extra_human_year() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2]


def test_first_fifteen_dog_years_should_give_one_human_year() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_next_nine_dog_years_should_give_one_more_human_year() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_every_five_next_dog_years_should_give_one_extra_human_year() -> None:
    result = get_human_age(29, 29)
    assert result == [3, 3]