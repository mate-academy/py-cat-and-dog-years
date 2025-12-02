from app.main import get_human_age


def test_return_0_if_animal_age_less_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_return_1_if_animal_age_equal_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_return_1_if_less_than_sum_first_and_second() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_return_2_if_animal_age_equal_sum_first_year_and_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_return_2_if_less_than_sum_first_second_and_4_5() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_return_3_if_equal_sum_first_second_and_4_5() -> None:
    assert get_human_age(28, 29) == [3, 3]
