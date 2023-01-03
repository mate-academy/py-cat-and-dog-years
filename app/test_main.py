import pytest
from app.main import get_human_age


def test_check_that_it_is_not_changed_with_previous_value() -> None:
    get_human_age(15, 15)
    assert get_human_age(28, 28) == [3, 2]


def test_resive_data_out_of_normal_range() -> None:
    assert get_human_age(-1, 0) == [0, 0]


def test_receives_an_incorrect_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 12.5)
