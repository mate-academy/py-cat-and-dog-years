from app.main import get_human_age

def test_cat_and_dog_age_should_be_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_age_should_be_equal() -> None:
    assert get_human_age(12, 12) == [0, 0]


def test_cat_and_dog_age_should_be_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_age_should_be_two() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_age_should_be_not_equal() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cat_and_dog_age_should_be_not_equal_high_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
