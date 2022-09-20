from app.main import get_human_age


def test_zero_ages():
    assert get_human_age(14, 14) == [0, 0]


def test_first_ages():
    assert get_human_age(15, 15) == [1, 1]


def test_second_ages():
    assert get_human_age(24, 24) == [2, 2]


def test_more_ages():
    assert get_human_age(28, 29) == [3, 3]


def test_result_should_is_list():
    assert isinstance(get_human_age(10, 10), list)
