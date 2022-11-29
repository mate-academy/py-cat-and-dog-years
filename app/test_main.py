from app.main import get_human_age


def test_get_human_age_return_zero_if_animals_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_14_or_less_cat_or_dog_years_should_convert_into_0_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(12, 13) == [0, 0]


def test_15_cat_or_dog_years_should_convert_into_1_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_27_cat_and_28_dog_years_should_convert_into_2_human_age() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_28_cat_and_29_dog_years_should_convert_into_2_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_get_human_age_calculates_correctly() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
