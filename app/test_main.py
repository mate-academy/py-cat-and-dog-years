from app.main import get_human_age


def test_cat_or_dog_years_less_then_15() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_first_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_next_9_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_every_4_cat_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_every_5_dog_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
