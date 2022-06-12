from app.main import get_human_age


def test_human_age_0_when_cat_dog_age_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_human_age_1_when_cat_dog_age_between_15_and_23():
    assert get_human_age(23, 23) == [1, 1]


def test_human_age_2_when_cat_dog_age_24():
    assert get_human_age(24, 24) == [2, 2]


def test_4_next_cat_years_after_24_return_extra_human_year():
    assert get_human_age(28, 28) == [3, 2]


def test_5_next_dog_years_after_24_return_extra_human_year():
    assert get_human_age(27, 29) == [2, 3]


def test_very_old_cat_dog_ages():
    assert get_human_age(100, 100) == [21, 17]
