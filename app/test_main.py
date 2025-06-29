from app.main import get_human_age


def test_cat_and_dog_have_not_human_years() -> None:
    cat = 14
    dog = 0
    assert get_human_age(cat, dog) == [0, 0]


def test_cat_and_dog_have_one_human_year() -> None:
    cat = 15
    dog = 15
    assert get_human_age(cat, dog) == [1, 1]


def test_cat_and_dog_have_one_human_year_yet() -> None:
    cat = 23
    dog = 23
    assert get_human_age(cat, dog) == [1, 1]


def test_cat_and_dog_have_two_human_year() -> None:
    cat = 24
    dog = 24
    assert get_human_age(cat, dog) == [2, 2]


def test_cat_and_dog_have_two_human_year_yet() -> None:
    cat = 27
    dog = 27
    assert get_human_age(cat, dog) == [2, 2]


def test_cat_and_dog_have_different_human_year() -> None:
    cat = 28
    dog = 28
    assert get_human_age(cat, dog) == [3, 2]


def test_cat_and_dog_have_different_human_year_yet() -> None:
    cat = 100
    dog = 100
    assert get_human_age(cat, dog) == [21, 17]
