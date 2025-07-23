from app.main import get_human_age

def test_cat_and_dog_zero_years():
    assert get_human_age(0, 0) == [0, 0]

def test_cat_and_dog_exactly_15():
    assert get_human_age(15, 15) == [1, 1]

def test_cat_and_dog_just_before_24():
    assert get_human_age(23, 23) == [1, 1]

def test_cat_and_dog_exactly_24():
    assert get_human_age(24, 24) == [2, 2]

def test_cat_28_dog_28():
    assert get_human_age(28, 28) == [3, 2]

def test_cat_and_dog_100():
    assert get_human_age(100, 100) == [21, 17]
