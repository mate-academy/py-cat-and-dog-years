from app.main import get_human_age


def test_dog_zero_cat_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_zero_years_end():
    assert get_human_age(14, 14) == [0, 0]


def test_first_years_begin():
    assert get_human_age(15, 15) == [1, 1]

def test_first_years_end():
    assert get_human_age(23, 23) == [1, 1]

def test_second_years_begin():
    assert get_human_age(24, 24) == [2, 2]


def test_second_years_end():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_thirt_dog_end_of_second():
    assert get_human_age(28, 28) == [3, 2]


def test_correct_calculation():
    assert get_human_age(100, 100) == [21, 17]
