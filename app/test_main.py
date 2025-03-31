from app.main import get_human_age


def test_dog_and_cat_not_human_year():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_has_but_dog_not_human_year():
    assert get_human_age(15, 14) == [1, 0]


def test_dog_has_but_cat_not_human_year():
    assert get_human_age(9, 15) == [0, 1]


def test_cat_and_dog_after_24_years():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_after_28_years():
    assert get_human_age(28, 28) == [3, 2]


def test_cat_and_dog_after_100_years():
    assert get_human_age(100, 100) == [21, 17]
