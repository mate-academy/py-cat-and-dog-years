from app.main import get_human_age


def test_income_zero_and_return_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_first_15_years():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_next_9_years():
    assert get_human_age(23, 23) == [1, 1]


def test_cat_next_every_4_years():
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_dog_next_every_5_years():
    assert get_human_age(29, 29) == [3, 3]
    assert get_human_age(36, 36) == [5, 4]


def test_incom_larg_numbers():
    assert get_human_age(36578, 74695) == [9140, 14936]
