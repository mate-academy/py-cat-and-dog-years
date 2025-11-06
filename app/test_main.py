from app.main import get_human_age


def test_first_dog_age():
    assert get_human_age(0, 0) == [0, 0]

def test_two_cat_age():
    assert get_human_age(0, 0) == [0, 0]

def test_tree_name_age():
    assert get_human_age(15, 15) == [1, 1]

def test_four_name_age():
    assert get_human_age(23, 23) == [1, 1]

def test_five_name_age():
    assert get_human_age(24, 24) == [2, 2]

def test_six_name_age():
    assert get_human_age(27, 27) == [2, 2]

def test_eight_name_age():
    assert get_human_age(28, 28) == [3, 2]

def test_nine_name_age():
    assert get_human_age(100, 100) == [21, 17]
