import pytest

from app.main import get_human_age


def test_first_15_dog_and_cat_years_give_1_human_year():
    assert get_human_age(14, 15) == [0, 1]


def test_every_9_next_years_for_dog_and_cat_give_1_more_human_year():
    assert get_human_age(23, 24) == [1, 2]


def test_every_5_dog_and_4_cat_years_give_1_extra_human_year():
    assert get_human_age(100, 100) == [21, 17]


def test_cat_or_dog_years_are_out_of_normal_years():
    assert get_human_age(-5, 0) == [0, 0]


def test_should_raise_error_when_passed_not_integer_to_age():
    with pytest.raises(TypeError):
        get_human_age("Hello", 3.5)
