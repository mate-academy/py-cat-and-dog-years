from app.main import get_human_age


def test_should_return_zeros_when_ages_less_than_14() -> None:
    cat_age = 14
    dog_age = 14
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_should_convert_first_15_animals_years_to_1_human_year() -> None:
    cat_age = 15
    dog_age = 15
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_should_convert_next_9_animals_years_to_1_more_human_year() -> None:
    cat_age = 24
    dog_age = 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_should_convert_every_4_next_cat_years_to_1_extra_human_year() -> None:
    cat_age = 28
    dog_age = 28
    assert get_human_age(cat_age, dog_age) == [3, 2]


def test_should_convert_every_5_next_dog_years_to_1_extra_human_year() -> None:
    cat_age = 100
    dog_age = 100
    assert get_human_age(cat_age, dog_age) == [21, 17]
