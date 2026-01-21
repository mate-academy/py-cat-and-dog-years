from app.main import get_human_age


def test_cats_and_dog_age_equals_zero() -> None:
    cat_age = 14
    dog_age = 14
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_cats_and_dog_age_equals_two() -> None:
    cat_age = 24
    dog_age = 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_cats_and_dog_age_equals_one() -> None:
    cat_age = 15
    dog_age = 15
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_cats_and_dog_age_equals_one_2() -> None:
    cat_age = 23
    dog_age = 23
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_cats_and_dog_age_equals_three() -> None:
    cat_age = 28
    dog_age = 29
    assert get_human_age(cat_age, dog_age) == [3, 3]


def test_cats_and_dog_age_more_three() -> None:
    cat_age = 100
    dog_age = 100
    assert get_human_age(cat_age, dog_age) == [21, 17]
