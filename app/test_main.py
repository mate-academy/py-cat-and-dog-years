from app.main import get_human_age

def test_should_return_zeros_when_ages_are_equals_zero():
    assert get_human_age(0, 0) == [0, 0]

def test_should_return_zeros_when_ages_less_than_fifteen():
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_zero_when_ages_are_negative():
    assert get_human_age(-2, -2) == [0, 0]

def test_cat_and_dog_age_15_years():
    assert get_human_age(15, 15) == [1, 1]

def test_cat_and_dog_age_24_years():
    assert get_human_age(24, 24) == [2, 2]

def test_cat_and_dog_age_28_years():
    assert get_human_age(28, 28) == [3, 2]

def test_should_work_correctly_with_unreal_number_of_years():
    assert get_human_age(1000, 1500) == [246, 297]