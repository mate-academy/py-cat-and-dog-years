from app.main import get_human_age
import pytest


def test_get_human_age_with_regular_ints() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(100, 100) == [21, 17]


def test_if_functions_take_wrong_type() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("12", "12")
        assert get_human_age(12.1, 12.1)


def test_negative_ints() -> None:
    assert get_human_age(-12, -12) == [0, 0]


def test_big_number() -> None:
    assert get_human_age(100000, 100000) == [24996, 19997]
