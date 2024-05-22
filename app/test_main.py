from app.main import get_human_age


def test_is_list_returned() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_is_length_of_list_equal_two() -> None:
    assert len(get_human_age(0, 0)) == 2


def test_are_values_of_list_integers() -> None:
    result = get_human_age(18, 18)
    assert isinstance(result[0], int) and isinstance(result[1], int)


def test_should_return_zeros_if_pets_ages_are_less_than_15() -> None:
    assert get_human_age(14, 12) == [0, 0]


def test_one_human_year_check() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_two_human_years_check() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_three_human_years_check() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_more_than_three_human_year_check() -> None:
    assert get_human_age(45, 57) == [7, 8]
