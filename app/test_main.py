from app.main import get_human_age
import pytest


def test_should_raise_error():
    cat_age = 0
    dog_age = 0
    with pytest.raises(ValueError):
        assert get_human_age(cat_age, dog_age)


def test_should_return_more_then_two_years():
    cat_age = 32
    dog_age = 29
    assert get_human_age(cat_age, dog_age) == [4, 3]


def test_should_return_equal_to_two_years():
    cat_age = 24
    dog_age = 24
    assert get_human_age(cat_age, dog_age) == [2, 2]


def test_if_age_less_then_zero():
    cat_age = -1
    dog_age = -1
    with pytest.raises(ValueError):
        assert get_human_age(cat_age, dog_age)


def test_should_raise_type_error():
    cat_age = "5"
    dog_age = "8"
    with pytest.raises(TypeError):
        assert get_human_age(cat_age, dog_age)
