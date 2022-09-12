import pytest

from app.main import get_human_age


def test_type_error():
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")


def test_first_15_cat_and_dog_years_give_1_human_year():
    assert get_human_age(7, 9) == [0, 0]


def test_the_next_9_cat_and_dog_years_give_1_more_human_year():
    assert get_human_age(17, 23) == [1, 1]


def test_every_4_next_cat_and_5_next_dog_years_give_1_extra_year():
    assert get_human_age(32, 44) == [4, 6]


def test_for_negative_ages():
    assert get_human_age(-2, -5) == [0, 0]


def test_for_zeroes_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_for_large_age():
    assert get_human_age(2350, 4320) == [583, 861]
