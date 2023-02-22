from app.main import get_human_age


def test_when_animals_age_less_15() -> None:
    assert get_human_age(0, 14) == [0, 0]


def test_when_animals_age_less_24() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_cat_age_more_24() -> None:
    assert get_human_age(28, 23) == [3, 1]


def test_dog_age_more_24() -> None:
    assert get_human_age(15, 29) == [1, 3]
