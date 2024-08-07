from app.main import get_human_age


def test_first_phase() -> None:
    cat_age = 14
    dog_age = 14
    res = get_human_age(cat_age, dog_age)
    assert res == [0, 0]


def test_rounding_age() -> None:
    cat_age = 23
    dog_age = 23
    res = get_human_age(cat_age, dog_age)
    assert res == [1, 1]


def test_second_phase() -> None:
    cat_age = 24
    dog_age = 24
    res = get_human_age(cat_age, dog_age)
    assert res == [2, 2]


def test_third_phase() -> None:
    cat_age = 28
    dog_age = 28
    res = get_human_age(cat_age, dog_age)
    assert res == [3, 2]


def test_old_age() -> None:
    cat_age = 100
    dog_age = 100
    res = get_human_age(cat_age, dog_age)
    assert res == [21, 17]
