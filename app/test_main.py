from app.main import get_human_age

def test_get_dog_and_cat_age_when_they_have_born():
    assert get_human_age(0, 0) == [0, 0]

def test_dog_and_cat_age_when_they_are_not_already_14():
    assert get_human_age(14, 14) == [0, 0]

def test_dog_and_cat_age_when_they_are_not_already_15():
    assert get_human_age(15, 15) == [1, 1]

def test_dog_and_cat_age_when_they_are_not_already_23():
    assert get_human_age(23, 23) == [1, 1]

def test_dog_and_cat_age_when_they_are_not_already_24():
    assert get_human_age(24, 24) == [2, 2]

def test_dog_and_cat_age_when_they_are_not_already_27():
    assert get_human_age(27, 27) == [2, 2]

def test_dog_and_cat_age_when_they_are_not_already_28():
    assert get_human_age(28, 28) == [3, 2]

def test_dog_and_cat_age_when_they_are_not_already_100():
    assert get_human_age(100, 100) == [21, 17]


