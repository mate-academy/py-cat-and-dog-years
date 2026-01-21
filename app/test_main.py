from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_age_up_to_15():
    assert get_human_age(14, 14) == [0, 0]


def test_age_up_to_24():
    assert get_human_age(23, 23) == [1, 1]


def test_age_up_to_28():
    assert get_human_age(27, 27) == [2, 2]


def test_extra_age_for_cats():
    assert get_human_age(28, 28) == [3, 2]


def test_extra_age_for_dogs():
    assert get_human_age(28, 29) == [3, 3]


def test_old_animals():
    assert get_human_age(100, 100) == [21, 17]
