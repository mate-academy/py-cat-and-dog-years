from app.main import get_human_age


def test_get_human_age_from_zero_cat_and_dog_age():
    cat_age = 0
    dog_age = 0

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [0, 0]


def test_get_first_human_year_from_cat_and_dog_age():
    cat_age = 15
    dog_age = 15

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [1, 1]


def test_get_second_human_year_from_cat_and_dog_age():
    cat_age = 24
    dog_age = 24

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [2, 2]
