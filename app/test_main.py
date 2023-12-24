from app.main import get_human_age
import pytest


def test_years_equal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_years_negative() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_firs_stage_of_growth() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_ear_take_dog_and_cat() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_stage_of_growth() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_ear_take_dog_and_cat() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_last_stage_equal_ear_cat_and_dog() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_third_stage_of_growth() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_long_life() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_receives_an_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", [12])
