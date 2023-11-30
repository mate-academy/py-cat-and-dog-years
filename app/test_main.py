from app.main import get_human_age


def test_if_age_animal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_if_animal_age_lass_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_if_animal_age_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_animal_age_is_integer() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_if_human_age_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_different_cat_and_dog_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_one_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]
