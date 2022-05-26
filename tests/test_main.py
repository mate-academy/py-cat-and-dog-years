import pytest

from app.main import get_human_age


def test_should_raise_TypeError_when_input_not_int():
    with pytest.raises(TypeError):
        assert get_human_age("4", "5")


def test_animal_ages_are_under_15():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_return_expected_ages_when_animals_are_beetwen_15_and_23():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_return_expected_ages_when_animals_are_beetwen_23_and_27():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_gives_extra_year_every_4_years_for_cars_after_24():
    assert get_human_age(28, 28) == [3, 2]


def test_gives_extra_year_every_5_years_for_dogs_after_24():
    assert get_human_age(28, 29) == [3, 3]

