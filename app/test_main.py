from app.main import get_human_age

def test_cat_and_dog_age_zero():
    assert get_human_age(0, 0) == [0, 0]

def test_cat_age_less_than_15():
    assert get_human_age(10, 0) == [1, 0]

def test_dog_age_less_than_15():
    assert get_human_age(0, 10) == [0, 1]

def test_cat_age_between_15_and_24():
    assert get_human_age(20, 0) == [2, 0]

def test_dog_age_between_15_and_24():
    assert get_human_age(0, 20) == [0, 2]

def test_cat_age_above_24():
    assert get_human_age(28, 0) == [3, 0]  # 15 -> 1, 9 -> 2, +4 -> 3
    assert get_human_age(32, 0) == [4, 0]  # 15 -> 1, 9 -> 2, +8 -> 4

def test_dog_age_above_24():
    assert get_human_age(0, 29) == [0, 3]  # 15 -> 1, 9 -> 2, +5 -> 3
    assert get_human_age(0, 34) == [0, 4]  # 15 -> 1, 9 -> 2, +10 -> 4

def test_cat_and_dog_mixed_ages():
    assert get_human_age(28, 34) == [3, 4]
    assert get_human_age(15, 15) == [1, 1]


