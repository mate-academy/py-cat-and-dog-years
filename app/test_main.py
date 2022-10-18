from app.main import get_human_age


def test_human_age_parameters_is_a_integer() -> None:
    test = get_human_age(10, 10)
    assert all([isinstance(test[0], int), isinstance(test[1], int)])


def test_should_return_0_if_parameters_are_negative() -> None:
    assert get_human_age(-5, -5) == [0, 0]


def test_should_return_0_if_parameters_is_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_if_parameters_is_under_15() -> None:
    assert get_human_age(7, 7) == [0, 0]


def test_should_return_1_if_parameters_from_15_to_23() -> None:
    assert get_human_age(20, 20) == [1, 1]


def test_correct_when_the_parameters_are_greater_than_23() -> None:
    assert get_human_age(75, 75) == [14, 12]


def test_should_return_first_year():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_different_values():
    assert get_human_age(28, 28) == [3, 2]
