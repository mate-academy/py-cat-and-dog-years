from app.main import get_human_age


def test_shoud_return_expected_result_with_discarded_remainder() -> None:
    assert get_human_age(32, 32) == [4, 3]


def test_shoud_return_expected_result_without_discarded_remainder() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_shoud_return_zeros_when_input_dates_equal_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_shoud_return_zeros_when_input_dates_negative_numbers() -> None:
    assert get_human_age(-23, -7) == [0, 0]


def test_shoud_return_zerous_when_input_date_less_then_15() -> None:
    assert get_human_age(12, 14) == [0, 0]


def test_shoud_return_one_when_input_date_less_then_24() -> None:
    assert get_human_age(23, 19) == [1, 1]


def test_shoud_return_expected_result_with_realu_large_numbers() -> None:
    assert get_human_age(150, 150) == [33, 27]
