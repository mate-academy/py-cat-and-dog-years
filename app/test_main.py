from app.main import get_human_age


def test_should_calculate_14_cat_or_dog_years_correctly() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_calculate_23_cat_or_dog_years_correctly() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_calculate_28_cat_and_29_dog_years_correctly() -> None:
    assert get_human_age(28, 29) == [2, 3]
