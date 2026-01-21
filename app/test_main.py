from app.main import get_human_age

def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]

def test_under_first_threshold():
    assert get_human_age(14, 14) == [0, 0]

def test_first_threshold():
    assert get_human_age(15, 15) == [1, 1]

def test_between_first_and_second_threshold():
    assert get_human_age(23, 23) == [1, 1]

def test_second_threshold_exact():
    assert get_human_age(24, 24) == [2, 2]

def test_between_second_and_third_threshold():
    assert get_human_age(27, 27) == [2, 2]

def test_cat_extra_human_years():
    assert get_human_age(28, 28) == [3, 2]


def test_dog_extra_human_years():
    assert get_human_age(15, 28) == [1, 2]
    assert get_human_age(24, 29) == [2, 3]
    assert get_human_age(24, 100) == [2, 17]

def test_large_values():
    assert get_human_age(100, 100) == [21, 17]
