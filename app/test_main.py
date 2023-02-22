import pytest

from app.main import get_human_age


def test_should_return_zeros_when_age_is_negative_number():
    assert get_human_age(-5, -10) == [0, 0]


def test_should_return_zeros_when_cat_and_dog_age_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_age_convert_when_age_less_than_24():
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_age_convert_when_age_less_than_28_and_greater_than_23():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_age_convert_when_age_greater_than_27():
    assert get_human_age(28, 28) == [3, 2]


def test_cat_and_dog_age_convert_when_age_is_a_big_number():
    assert get_human_age(100, 100) == [21, 17]


def test_should_raise_error():
    with pytest.raises(TypeError):
        get_human_age("15", "25")