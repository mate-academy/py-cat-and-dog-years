from app.main import get_human_age


def test_two_parameters_equal_to_zero() -> None:
    assert (get_human_age(0, 0) == [0, 0])


def test_one_parameter_equal_to_zero() -> None:
    assert (get_human_age(0, 21) == [0, 1])


def test_float_value_of_parameters() -> None:
    assert (get_human_age(23.2, 25) == [1, 2])


def test_very_big_value_of_parameters() -> None:
    assert (get_human_age(110324, 13455) == [27577, 2688])


def test_negative_value_of_parameter() -> None:
    assert (get_human_age(-15, 54) == [0, 8])
