from app.main import get_human_age


def test_get_human_age_both_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_both_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_both_15():
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_both_between_15_and_24():
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_both_24():
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_both_between_24_and_27():
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_28_dog_27():
    assert get_human_age(28, 27) == [3, 2]


def test_get_human_age_cat_100_dog_100():
    assert get_human_age(100, 100) == [21, 17]
