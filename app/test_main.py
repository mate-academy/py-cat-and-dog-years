from app.main import get_human_age


def test_should_return_zero_when_age_less_than_15() -> None:
    cat_age = 14
    dog_age = 14
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_should_return_one_when_age_is_15() -> None:
    cat_age = 15
    dog_age = 15
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_should_return_one_when_age_less_than_24() -> None:
    cat_age = 23
    dog_age = 23
    assert get_human_age(cat_age, dog_age) == [1, 1]


def test_should_return_two_when_age_is_24() -> None:
    cat_age = 24
    dog_age = 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_should_return_two_when_cat_age_less_28_and_dog_age_less_29() -> None:
    cat_age = 27
    dog_age = 28
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_should_return_three_when_cat_age_is_28_and_dog_age_is_29() -> None:
    cat_age = 28
    dog_age = 29
    assert get_human_age(cat_age, dog_age) == [3, 3]
