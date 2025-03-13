from app.main import get_human_age


def test_convert_to_human_age_if_dog_and_cat_is_0():
    res = get_human_age(0, 0)
    assert res == [0, 0]


def test_convert_to_human_age_if_dog_and_cat_under_15():
    res = get_human_age(14, 14)
    assert res == [0, 0]


def test_convert_to_human_age_if_dog_and_cat_is_15():
    res = get_human_age(15, 15)
    assert res == [1, 1]


def test_convert_to_human_age_if_dog_and_cat_over_15_next_9():
    res = get_human_age(24, 24)
    assert res == [2, 2]


def test_convert_to_human_age_dog_more_5_extra_year():
    res = get_human_age(28, 28)
    assert res == [3, 2]


def test_convert_to_human_age_if_dog_and_cat_is_100():
    res = get_human_age(100, 100)
    assert res == [21, 17]
