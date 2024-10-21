from app.main import get_human_age


def test_15_years_animals_is_1_human() -> None:
    assert get_human_age(15, 14) == [1, 0]


def test_15_plus_9_years_is_1_human() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_28_29_cat_dog_is_3_human() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_remainder_should_discarded() -> None:
    assert get_human_age(100.1, 100.5) == [21, 17]
