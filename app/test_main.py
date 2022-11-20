from app.main import get_human_age


def get_correct_age_for_animals_with_normal_values():
    assert (
        get_human_age(28, 28) == [3, 2]
    )
    assert (
        get_human_age(100, 100) == [21, 17]
    )


def get_correct_age_for_animals_with_out_of_normal_range():
    assert (
        get_human_age(-100, -100) == [0, 0]
    )
    assert (
        get_human_age(999, 999) == [245, 197]
    )


def get_correct_data_type_for_function_or_raise_error():
    try:
        assert isinstance(get_human_age(1, 3), list)
    except AssertionError:
        raise TypeError("Values should be int type")


def check_if_previous_number_did_not_changed():
    human_age = get_human_age(34,90)
    assert (
        human_age[0] == 34 and human_age[1] == 90
    )
