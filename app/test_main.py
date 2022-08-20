from app.main import get_human_age


def test_cat_dog_human_zero_years():
    assert get_human_age(0, 0) == [0, 0]


def test_cat_dog_end_zero_human_year():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_dog_start_first_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_cat_dog_end_first_human_year():
    assert get_human_age(23, 23) == [1, 1]


def test_cat_dog_start_second_human_year():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_end_second_human_year():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_start_third_human_year_dog_end_second_human_year():
    assert get_human_age(28, 28) == [3, 2]


def test_cat_dog_various_human_years():
    assert get_human_age(100, 100) == [21, 17]