from app.main import get_human_age


def test_zero_ages():
    assert get_human_age(cat_age=0, dog_age=0) == [0, 0]


def test_just_before_first_year():
    assert get_human_age(cat_age=14, dog_age=14) == [0, 0]


def test_first_human_year_threshold():
    assert get_human_age(cat_age=15, dog_age=15) == [1, 1]


def test_before_second_human_year():
    assert get_human_age(cat_age=23, dog_age=23) == [1, 1]


def test_exact_second_human_year():
    assert get_human_age(cat_age=24, dog_age=24) == [2, 2]


def test_between_second_and_third_year():
    assert get_human_age(cat_age=27, dog_age=27) == [2, 2]
