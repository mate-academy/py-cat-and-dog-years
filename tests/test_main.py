from app.main import get_human_age


def test_human_age_is_zero_when_cat_or_dog_age_is_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_human_age_is_zero_when_cat_or_dog_age_is_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_human_age_is_1_when_cat_or_dog_age_is_15():
    assert get_human_age(15, 15) == [1, 1]


def test_human_age_is_1_when_cat_or_dog_age_is_between_15_and_23():
    assert get_human_age(23, 23) == [1, 1]


def test_human_age_is_2_when_cat_or_dog_age_is_24():
    assert get_human_age(24, 24) == [2, 2]


def test_human_age_is_3_when_cat_age_is_28_but_is_2_when_dog_age_is_28():
    assert get_human_age(28, 28) == [3, 2]


def test_human_age_when_cat_or_dog_age_is_big():
    assert get_human_age(100, 100) == [21, 17]
