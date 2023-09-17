from app.main import get_human_age

def test_when_value_less_or_equal_14():
    assert get_human_age(14, 14) == [0, 0]


def test_when_value_more_15_and_less_23():
    assert get_human_age(22, 22) == [1, 1]


def test_when_value_more_24_and_less_28():
    assert get_human_age(27, 27) == [2, 2]


def test_when_value_equal_28():
    assert get_human_age(28, 28) == [3, 2]


def test_when_value_equal_100():
    assert get_human_age(100, 100) == [21, 17]
