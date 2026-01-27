from app.main import get_human_age

def test_get_human_age_less_than_one():
    assert get_human_age(14,14) == [0, 0]


def test_get_human_age_without_randing():
    assert get_human_age(28,29) == [3, 3]


def test_get_human_age_with_randing():
    assert get_human_age(29,30) == [3, 3]


def test_pet_age_convert_should_equal_1():
    assert get_human_age(15,15) == [1, 1]


def test_pet_age_convert_should_equal_one():
    assert get_human_age(23,23) == [1, 1]