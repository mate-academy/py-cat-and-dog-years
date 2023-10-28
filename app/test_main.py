from app.main import get_human_age


def test_should_return_zero_when_dog_and_cat_year_equal_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_dog_and_cat_year_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_dog_and_cat_year_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_dog_and_cat_year_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_dog_and_cat_year_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_dog_and_cat_year_less_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_2_and_3_when_dog_and_cat_year_equal_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_when_dog_and_cat_year_equal_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
