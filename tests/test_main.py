from app.main import get_human_age, convert_to_human


def test_return_zeroes_if_animals_age_equal_to_0():
    assert get_human_age(0, 0) == [0, 0]


def test_return_zeros_if_animals_age_less_then_15():
    assert get_human_age(5, 1) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_animals_age_more_then_15():
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(100, 100) == [21, 17]
