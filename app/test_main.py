from app.main import get_human_age


def test_check_human_age_when_animal_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_check_human_age_when_animal_age_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_check_human_age_when_animal_age_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_check_human_age_when_animal_age_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_check_human_age_when_animal_age_equal_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_check_human_age_when_cat_and_dog_age_equal_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_check_human_age_when_cat_and_dog_age_equal_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
