from app.main import get_human_age


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
    try:
        assert isinstance(get_human_age(1, 3), list)
    except AssertionError:
        raise TypeError("Values should be int type")


def test_check_if_previous_number_did_not_change() -> None:
    result = get_human_age(22, 100)
    result1 = get_human_age(22, 100)
    assert (
        result is not result1
    )
