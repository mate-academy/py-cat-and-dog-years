from app.main import get_human_age


def test_give_0_cat_dog_year() -> None:
    cat = 0
    dog = 0
    assert get_human_age(cat, dog) == [0, 0]


def test_give_20_cat_20_dog_year() -> None:
    cat = 20
    dog = 20
    assert get_human_age(cat, dog) == [1, 1]


def test_give_200_cat_200_dog_year() -> None:
    cat = 200
    dog = 200
    assert get_human_age(cat, dog) == [46, 37]


def test_give_negative_year() -> None:
    cat = -200
    dog = -200
    assert get_human_age(cat, dog) == [0, 0]


def test_cat_14_dog_23() -> None:
    cat = 14
    dog = 23
    assert get_human_age(cat, dog) == [0, 1]
