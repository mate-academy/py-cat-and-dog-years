from app.main import get_human_age


def test_from_0_to_14_years_are_0_in_humans_years() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_from_15_to_23_years_are_1_in_humans_years() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_from_24_to_27_years_are_2_in_humans_years() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_cats_28_years_are_3_humans_years_28_dogs_years_are_2_humans() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cats_100_years_are_21_humans_years_100_dogs_years_are_17_humans() -> None:  # noqa: E501
    assert get_human_age(100, 100) == [21, 17]
