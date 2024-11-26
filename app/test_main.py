from app.main import get_human_age


def test_cat_and_dog_years_zero() -> None:
    cat_age = 0
    dog_age = 0
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]


def test_convert_years() -> None:
    cat_age = 100
    dog_age = 100
    result = get_human_age(cat_age, dog_age)
    assert result == [21, 17]


def test_convert_under_fifteen() -> None:
    cat_age = 14
    dog_age = 14
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]


def test_convert_under_23() -> None:
    cat_age = 23
    dog_age = 23
    result = get_human_age(cat_age, dog_age)
    assert result == [1, 1]
