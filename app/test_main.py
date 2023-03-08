from app.main import get_human_age


def test_should_return_zeroes_when_integers_are_zeroes():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeroes_when_integers_less_first_year():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_integers_less_second_year():
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_integers_less_third_year():
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_validates_years_for_each_animal():
    assert get_human_age(28, 28) == [3, 2]


def test_should_check_huge_numbers():
    assert get_human_age(100, 100) == [21, 17]
