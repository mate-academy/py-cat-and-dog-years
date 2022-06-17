from app.main import get_human_age


def test_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_first():
    assert get_human_age(15, 15) == [1, 1]


def test_next():
    assert get_human_age(23, 23) == [1, 1]


def test_second():
    assert get_human_age(27, 27) == [2, 2]


def test_three_cats():
    assert get_human_age(28, 28) == [3, 2]


def test_one_hundred():
    assert get_human_age(100, 100) == [21, 17]
