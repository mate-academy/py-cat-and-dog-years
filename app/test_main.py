import pytest
from app.main import get_human_age


def test_pets_age_negative_or_below_15_should_return_zero_human_age() -> None:
    assert get_human_age(-20, -20) == [0, 0]
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_pets_age_from_15_to_23_should_return_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_pets_age_from_24_to_27_should_return_2_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_cat_after_28_should_increment_human_age_every_4_years_by_1() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(54, 10) == [9, 0]
    assert get_human_age(56, 15) == [10, 1]


def test_dog_after_29_should_increment_human_age_every_5_years_by_1() -> None:
    assert get_human_age(24, 30) == [2, 3]
    assert get_human_age(10, 53) == [0, 7]
    assert get_human_age(15, 56) == [1, 8]


def test_cat_and_dog_unreal_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
    assert get_human_age(500, 500) == [121, 97]


def test_should_raise_type_error_when_input_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", 1.1)
