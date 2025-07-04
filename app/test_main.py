from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_convert_cat_and_dog_age_under_15() -> None:
    assert get_human_age(10, 10) == [0, 0]


def test_should_convert_cat_and_dog_age_under_24() -> None:
    assert get_human_age(20, 20) == [1, 1]


def test_should_convert_cat_age_above_24() -> None:
    assert get_human_age(39, 0) == [5, 0]


def test_should_convert_dog_age_above_24() -> None:
    assert get_human_age(0, 34) == [0, 4]


def test_should_convert_both_cat_and_dog_ages() -> None:
    assert get_human_age(28, 29) == [3, 3]
