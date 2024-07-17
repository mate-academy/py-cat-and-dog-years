from app.main import get_human_age


def test_zeroes_years():
    cat_age = 0
    dog_age = 0

    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_negative_years():
    cat_age = -1
    dog_age = -2

    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_normal_years():
    cat_age = 14
    dog_age = 45

    assert get_human_age(cat_age, dog_age) == [0, 6]


def test_normal_years2():
    cat_age = 56
    dog_age = 23

    assert get_human_age(cat_age, dog_age) == [10, 1]


def test_big_and_not_rounded_years():
    cat_age = 11893
    dog_age = 8919

    assert get_human_age(cat_age, dog_age) == [2969, 1781]

