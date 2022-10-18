import pytest
from app.main import get_human_age


def test_should_return_expected_animal_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_when_cat_age_is_less_than_0() -> None:
    assert get_human_age(-10, 100) == [0, 17]


def test_when_dog_age_is_less_than_0() -> None:
    assert get_human_age(100, -1) == [21, 0]


def test_should_raise_error_if_incorrect_data_type() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("sf", [])
