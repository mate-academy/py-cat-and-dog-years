from app.main import get_human_age


def test_0_when_the_first_years_are_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_first_years():
    assert get_human_age(15, 15) == [1, 1]


def test_1_when_the_second_years_are_less_than_24():
    assert get_human_age(23, 23) == [1, 1]


def test_second_years():
    assert get_human_age(24, 24) == [2, 2]


def test_2_when_the_each_years_are_less_than_28():
    assert get_human_age(27, 27) == [2, 2]


def test_each_years():
    assert get_human_age(28, 29) == [3, 3]
