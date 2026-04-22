from app.main import get_human_age


def test_cat_and_dog_age_age_less_then_15() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_cat_and_dog_age_less_then_24() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_cat_and_dog_age_is_28() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_cat_and_dog_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
