from app.main import get_human_age


def test_get_human_age_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_15():
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exact_15():
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_below_24():
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_exact_24():
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_below_28():
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_exact_28():
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_ages():
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_negative():
    assert get_human_age(-1, -1) == [0, 0]
