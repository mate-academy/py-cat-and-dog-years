from app.main import get_human_age

def test_check_animal_to_human_is_zero():
    assert get_human_age(0, 0) == [0,0]


def test_check_animal_to_human_is_one():
    assert get_human_age(15, 15) == [1, 1]


def test_check_animal_to_human_is_two():
    assert get_human_age(27, 27) == [2, 2]


def test_check_cat_to_human_and_dog_to_human_are_different():
    assert get_human_age(28, 28) == [3, 2]


def test_extra_human_years():
    assert get_human_age(100, 100) == [21, 17]