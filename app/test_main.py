from app.main import get_human_age


def test_when_the_years_are_a_negative_number():
    assert get_human_age(-1, -4) == [0, 0]


def test_0_when_the_first_years_are_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_1_when_the_first_years_are_equal_15():
    assert get_human_age(15, 15) == [1, 1]


def test_1_when_the_second_years_are_less_than_24():
    assert get_human_age(23, 23) == [1, 1]


def test_2_when_the_second_years_are_equal_24():
    assert get_human_age(24, 24) == [2, 2]


def test_2_when_the_each_years_are_less_than_28():
    assert get_human_age(27, 27) == [2, 2]


def test_3_when_the_each_years_are_equal_28_and_29():
    assert get_human_age(28, 29) == [3, 3]


def test_when_the_years_are_large_numbers():
    assert get_human_age(100, 100) == [21, 17]
