from app.main import get_human_age


def test_correct_age_calculation() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_big_number() -> None:
    assert get_human_age(416, 514) == [100, 100]


def test_cat_is_older() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_is_older() -> None:
    assert get_human_age(15, 28) == [1, 2]


def test_not_enough() -> None:
    assert get_human_age(5, 5) == [0, 0]
