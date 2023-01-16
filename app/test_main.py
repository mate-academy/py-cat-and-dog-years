from app.main import get_human_age
import pytest


def test_age_equal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_15() -> None:
    assert (get_human_age(14, 14) == [0, 0])


def test_age_equal_15() -> None:
    assert (get_human_age(15, 15) == [1, 1])


def test_age_more_15_less_24() -> None:
    assert (get_human_age(23, 23) == [1, 1])


def test_age_equal_24() -> None:
    assert (get_human_age(24, 24) == [2, 2])


def test_age_more_24_less_27() -> None:
    assert (get_human_age(27, 28) == [2, 2])


def test_age_equal_28() -> None:
    assert (get_human_age(28, 28) == [3, 2])


def test_age_less_zero() -> None:
    assert (get_human_age(-1, -10) == [0, 0])


def test_receives_an_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", [12])
