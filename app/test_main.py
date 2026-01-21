from app.main import get_human_age

def test_get_human_age_returns_zero_when_given_low_cat_dog_age():
    assert get_human_age(0, 14) == [0, 0]

def test_get_human_age_returns_1_when_given_15_cat_dog_age():
    assert get_human_age(15, 15) == [1, 1]

def test_get_human_age_returns_2_when_given_25_dog_age():
    assert get_human_age(25, 25) == [2, 2]

def test_get_human_age_returns_3_when_given_28_cat_age():
    assert get_human_age(28, 28) == [3, 2]

def test_get_human_age_returns_3_when_given_29_dog_age():
    assert get_human_age(29, 29) == [3, 3]

def test_get_human_age_correctly_counts_high_values():
    assert get_human_age(100, 100) == [21, 17]