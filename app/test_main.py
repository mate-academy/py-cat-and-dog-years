from app.main import get_human_age


def test_should_return_zeros_when_zero_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_when_age_less_than_first_threshold():
    assert get_human_age(14, 14) == [0,0]


def test_should_return_ones_when_age_equal_to_first_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_ones_when_age_between_first_and_second_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_twos_when_age_equal_to_sum_of_first_and_second_thresholds():
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_twos_when_age_just_above_second_threshold():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_different_animal_age_when_same_years():
    assert get_human_age(28, 28) == [3, 2]


def test_high_ages():
    assert get_human_age(100, 100) == [21, 17]
