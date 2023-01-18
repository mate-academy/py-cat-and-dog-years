import pytest
from app.main import get_human_age


def test_check_that_it_is_not_changed_with_previous_value() -> None:
    get_human_age(15, 15)
    assert get_human_age(28, 28) == [3, 2]


def test_resive_data_out_of_normal_range() -> None:
    assert get_human_age(-1, 0) == [0, 0]


def test_resive_data_of_large_numbers() -> None:
    assert get_human_age(1000, 0) == [246, 0]


def test_receives_an_str_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 1)


def test_receives_an_float_type_of_data() -> None:
    assert get_human_age(25.5, 45.1) == [2, 6]


def test_receives_an_list_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age([], 1)


def test_receives_an_dict_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age({}, 1)


def test_receives_an_set_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age((), 1)
