from app.main import get_human_age


def test_14_cat_and_dog_years_convert_into_0() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_15_cat_and_dog_years_convert_into_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_23_cat_and_dog_years_convert_into_1() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_cat_and_dog_years_convert_into_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_27_and_28_cat_and_dog_years_convert_into_2() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_28_and_29_cat_and_dog_years_convert_into_3() -> None:
    assert get_human_age(28, 29) == [3, 3]
