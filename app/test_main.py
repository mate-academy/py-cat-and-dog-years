from app.main import get_human_age


def test_14_cat_dog_years_should_convert_into_0_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_24_cat_dog_years_should_convert_into_2_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_23_cat_dog_years_should_convert_into_1_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_27_28_cat_dog_years_should_convert_into_2_human_age() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_15_cat_dog_years_should_convert_into_1_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_28_29_cat_dog_years_should_convert_into_3_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]