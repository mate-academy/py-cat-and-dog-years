from app.main import get_human_age


def test_should_return_zeros_list_for_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_list_for_last_begin_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_ones_list_for_first_middle_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_ones_list_for_last_middle_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_twos_list_for_first_end_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_valid_list_for_next_end_years() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(64, 56) == [12, 8]
    assert get_human_age(100, 100) == [21, 17]
