from app.main import get_human_age


def test_zero_values_for_cat_and_dog_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_age_before_14_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_age_when_it_is_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_age_before_24_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_age_when_it_is_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_age_before_28_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_age_when_it_is_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cat_and_dog_age_when_it_is_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
