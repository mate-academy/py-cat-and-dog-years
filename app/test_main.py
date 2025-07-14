from app.main import get_human_age

def test_correct_age_calculation():
    assert get_human_age(15, 15) == [1, 1]

def test_age_is_zero():
    assert get_human_age(0, 0) == [0, 0]

def test_big_number():
    assert get_human_age(416, 514) == [100, 100]

def test_cat_is_older():
    assert get_human_age(28, 28) == [3, 2]

def test_dog_is_older():
    assert get_human_age(15, 28) == [1, 2]

def test_not_enough():
    assert get_human_age(5, 5) == [0, 0]
