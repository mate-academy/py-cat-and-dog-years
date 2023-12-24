from app.main import get_human_age


def test_if_all_arguments_are_int():
    assert get_human_age(14, 14) == [0, 0]

    assert get_human_age(27, 27) == [2, 2]


def test_if_arguments_are_large():
    assert get_human_age(527, 324) == [127, 62]


def test_func_return_list():
    assert isinstance(get_human_age(0, 0), list)


def test_if_arguments_equal_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_if_arguments_equal_negative_value():
    assert get_human_age(-2, -5) == [0, 0]
