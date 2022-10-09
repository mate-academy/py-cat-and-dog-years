from app.main import get_human_age


def test_human_age_parameters_is_a_integer():
    test = get_human_age(10, 10)
    assert all([isinstance(test[0], int), isinstance(test[1], int)])


def test_should_return_0_if_parameters_are_negative():
    assert get_human_age(-5, -5) == [0, 0]


def test_should_return_0_if_parameters_is_0():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_if_parameters_is_under_15():
    assert get_human_age(7, 7) == [0, 0]


def test_should_return_1_if_parameters_from_15_to_23():
    assert get_human_age(20, 20) == [1, 1]


def test_correct_when_the_parameters_are_greater_than_23():
    assert get_human_age(75, 75) == [14, 12]
