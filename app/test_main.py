from app.main import get_human_age

def test_func_return_basic_value():
    assert get_human_age(0, 0) == [0, 0]

def test_first_up_age():
    assert get_human_age(15, 15) == [1, 1]

def test_age_low_15():
    assert get_human_age(14, 14) == [0, 0]

def test_age_high_15():
    assert get_human_age(24, 24) == [2, 2]

def test_age_low_dog_age():
    assert get_human_age(28, 24) == [3, 2]

def test_human_age_100():
    assert get_human_age(100, 100) == [21, 17]

