from app.main import get_human_age


def test_if_0_years_equal_0_human_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_if_less_than_15_years_turn_into_0_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_if_15_years_turn_into_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_if_less_than_24_years_turn_into_1_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_if_24_years_turn_into_2_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_if_less_than_28_years_turn_into_2_human_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_if_28_cat_years_equal_3_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_if_29_dog_years_equal_3_human_years() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_100_animal_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
