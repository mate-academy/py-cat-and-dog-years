import pytest
from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_after_second_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_have_different_rules() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_negative_input_values() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)


def test_incorrect_types_string() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", 10)  # type: ignore


def test_incorrect_types_float() -> None:
    with pytest.raises(TypeError):
        get_human_age(10.5, 10)  # type: ignore
