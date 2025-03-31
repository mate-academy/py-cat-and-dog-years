from app.main import get_human_age


def test_if_cats_age_is_0_and_dogs_age_is_0() -> None:
    result_of_func = get_human_age(0, 0)
    assert result_of_func == [0, 0]


def test_if_cats_age_is_14_and_dogs_age_is_14() -> None:
    result_of_func = get_human_age(14, 14)
    assert result_of_func == [0, 0]


def test_if_cats_age_is_15_and_dogs_age_is_15() -> None:
    result_of_func = get_human_age(15, 15)
    assert result_of_func == [1, 1]


def test_if_cats_age_is_23_and_dogs_age_is_23() -> None:
    result_of_func = get_human_age(23, 23)
    assert result_of_func == [1, 1]


def test_if_cats_age_is_24_and_dogs_age_is_24() -> None:
    result_of_func = get_human_age(24, 24)
    assert result_of_func == [2, 2]


def test_if_cats_age_is_27_and_dogs_age_is_27() -> None:
    result_of_func = get_human_age(27, 27)
    assert result_of_func == [2, 2]


def test_if_cats_age_is_28_and_dogs_age_is_28() -> None:
    result_of_func = get_human_age(28, 28)
    assert result_of_func == [3, 2]


def test_if_cats_age_is_100_and_dogs_age_is_100() -> None:
    result_of_func = get_human_age(100, 100)
    assert result_of_func == [21, 17]
