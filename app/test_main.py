from app.main import get_human_age


def test_should_return_zero_if_years_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_if_years_lt_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_if_years_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_if_years_lt_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_if_years_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_if_years_lt_27_28_for_cat_dog() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_3_if_years_lt_28_29_for_cat_dog() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_for_big_years_numbers() -> None:
    assert get_human_age(80, 80) == [16, 13]


def test_should_separate_count_for_dog_cat_years() -> None:
    assert get_human_age(50, 12) == [8, 0]
