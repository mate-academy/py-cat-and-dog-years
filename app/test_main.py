from app.main import get_human_age

def test_age_zero_equals_zero():
    assert get_human_age(0,0) == [0, 0]

def test_age_lower_than_first_year_equals_zero():
    assert get_human_age(14,13) == [0, 0]

def test_age_first_year_equals_one():
    assert get_human_age(15,15) == [1, 1]

def test_age_24_should_return_1_for_both():
    assert get_human_age(23,23) == [1, 1]

def test_age_24_should_return_2_for_both():
    assert get_human_age(24,24) == [2, 2]

def test_age_27_cat_28_dog_equals_2_human():
    assert get_human_age(27,28) == [2, 2]

def test_age_28_cat_29_dog_equals_3_human():
    assert get_human_age(28,29) == [3, 3]
