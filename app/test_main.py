from app.main import get_human_age
import pytest


def test_should_correctly_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(5.5, "10")


def test_should_convert_correctly_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_convert_correctly_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_convert_correctly_each_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_get_human_age_with_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_list() -> None:
    result = get_human_age(10, 10)
    assert isinstance(result, list)
