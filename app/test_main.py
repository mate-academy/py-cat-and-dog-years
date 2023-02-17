import pytest
from app.main import get_human_age


def test_should_return_list_of_integers() -> None:
    assert (isinstance(get_human_age(27, 27), list)
            and isinstance(get_human_age(27, 27)[0], int)
            and isinstance(get_human_age(27, 27)[1], int))


def test_should_return_zeros_when_take_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_take_negative() -> None:
    assert get_human_age(-10, -10) == [0, 0]


def test_should_return_zeros_when_age_lower_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_ones_when_age_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_when_age_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_three_when_age_equal_28_and_29() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_raise_error_when_take_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("15.0", "15.0")
