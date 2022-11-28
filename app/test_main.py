import pytest

from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(88, 88) == [18, 14]


def test_if_output_changed_with_previous_value() -> None:
    result_1 = get_human_age(30, 33)
    result_2 = get_human_age(30, 33)
    assert result_1 is not result_2


def test_if_age_is_zero() -> None:
    assert get_human_age(0, 22) == [0, 1]


def test_if_age_is_negative() -> None:
    assert get_human_age(-15, -31) == [0, 0]


def test_if_age_number_is_too_big() -> None:
    assert get_human_age(250, 250) == [58, 47]


def test_if_age_value_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("twenty", 25)
