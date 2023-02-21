from app.main import get_human_age
import pytest


def test_should_return_correct_age_for_young_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
def test_should_return_correct_age_for_the_next_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]
def test_should_return_correct_age_for_the_next_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]
def test_should_return_correct_age_for_the_next_cat_years() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_should_return_correct_age_for_the_next_dog_years() -> None:
    assert get_human_age(29, 29) == [3, 3]

def test_should_received_correct_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "4")