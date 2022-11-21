from app.main import get_human_age
import pytest


def test_get_correct_age_for_animals_with_normal_values() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    )
    assert (
        get_human_age(100, 100) == [21, 17]
    )


def test_get_correct_age_for_animals_with_out_of_normal_range() -> None:
    assert (
        get_human_age(-100, -100) == [0, 0]
    )
    assert (
        get_human_age(999, 999) == [245, 197]
    )


def test_get_correct_data_type_for_function_or_raise_error() -> None:
    with pytest.raises(TypeError):
        assert get_human_age([], ()) is not list


def test_check_if_previous_number_did_not_change() -> None:
    assert (
        get_human_age(22, 100) is not get_human_age(22, 100)
    )
