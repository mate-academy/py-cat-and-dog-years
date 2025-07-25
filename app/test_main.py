from app.main import get_human_age


def test_return_zeros_when_input_0():
    assert get_human_age(0, 0) == [0, 0]


def test_return_zeros_when_input_14():
    assert get_human_age(14, 14) == [0, 0]


def test_return_ones_when_input_15():
    assert get_human_age(15, 15) == [1, 1]


def test_return_ones_when_input_23():
    assert get_human_age(23, 23) == [1, 1]


def test_return_twos_when_input_24():
    assert get_human_age(24, 24) == [2, 2]


def test_return_threes_when_input_28_29():
    assert get_human_age(28, 29) == [3, 3]


def test_return_21_17_when_input_100():
    assert get_human_age(100, 100) == [21, 17]


def test_return_zeros_when_input_lesser_0():
    assert get_human_age(-1, -1) == [0, 0]
