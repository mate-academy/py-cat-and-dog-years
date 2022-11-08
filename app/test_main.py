from app.main import get_human_age
import pytest


def test_zero_values() -> None:
    assert get_human_age(0, 0) == [0, 0], "test zero values"


def test_should_convert_into_zero_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0], "test convert to [0, 0] human ages"


def test_should_convert_into_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1], "test convert to [1, 1] human ages"


def test_should_convert_into_one_human_age2() -> None:
    assert get_human_age(23, 23) == [1, 1], "test convert to [1, 1] human ages"


def test_should_convert_into_two_human_ages() -> None:
    assert get_human_age(24, 24) == [2, 2], "test convert to [2, 2] human ages"


def test_should_convert_into_two_human_ages2() -> None:
    assert get_human_age(27, 28) == [2, 2], "test convert to [2, 2] human ages"


def test_negative_values() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_large_values() -> None:
    assert get_human_age(1000000000, 1000000000) == [249999996, 199999997]


def test_incorrect_type_values() -> None:
    with pytest.raises(TypeError):
        get_human_age("6", "12")
