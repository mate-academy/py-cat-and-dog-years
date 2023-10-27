from app.main import get_human_age


def test_should_add_zeroes_when_animal_age_is_less_then_15() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_should_add_one_when_animal_age_is_less_than_24() -> None:
    result = get_human_age(23, 23)
    assert result == [1, 1]


def test_should_add_one_year_when_cat_age_is_less_than_28_dog_age_less_than_29(

) -> None:
    result = get_human_age(27, 28)
    assert result == [2, 2]


def test_should_add_one_year_when_cat_age_is_more_than_27_dog_age_more_than_28(

) -> None:
    result = get_human_age(28, 29)
    assert result == [3, 3]
