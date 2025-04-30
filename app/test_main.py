from app.main import get_human_age


def test_get_human_age_2() -> None:
    cat_age = 0
    dog_age = 0
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]


def test_get_human_age_3() -> None:
    cat_age = 15
    dog_age = 15
    result = get_human_age(cat_age, dog_age)
    assert result == [1, 1]


def test_get_human_age_4() -> None:
    cat_age = 23
    dog_age = 23
    result = get_human_age(cat_age, dog_age)
    assert result == [1, 1]


def test_get_human_age_5() -> None:
    cat_age = 24
    dog_age = 24
    result = get_human_age(cat_age, dog_age)
    assert result == [2, 2]


def test_get_human_age_6() -> None:
    cat_age = 27
    dog_age = 27
    result = get_human_age(cat_age, dog_age)
    assert result == [2, 2]


def test_get_human_age_7() -> None:
    cat_age = 28
    dog_age = 28
    result = get_human_age(cat_age, dog_age)
    assert result == [3, 2]


def test_get_human_age_8() -> None:
    cat_age = 100
    dog_age = 100
    result = get_human_age(cat_age, dog_age)
    assert result == [21, 17]
