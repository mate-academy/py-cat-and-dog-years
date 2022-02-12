from app.main import get_human_age


def test_if_age_in_function_equal_to_0():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_is_between_15():
    assert get_human_age(15, 15) == [1, 1]


def test_checking_differences_between_low_numbers():
    assert get_human_age(28, 28) == [3, 2]


def test_checking_a_differences_between_large_numbers():
    assert get_human_age(100, 100) == [21, 17]
