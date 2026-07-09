from app.main import get_human_age

def test_one_year_equals_fifteen():
    assert get_human_age(15, 15) == [1, 1]

def test_less_than_one_year_equals_zero():
    assert get_human_age(5, 5) == [0, 0]

def test_different_values_return_different_lists():
    assert get_human_age(17, 14) == [1, 0]
    assert get_human_age(1, 25) == [0, 2]

def test_func_rounds_floats_into_integers():
    assert get_human_age(9.162, 23.739) == [0, 1]
    assert get_human_age(27.54, 30.44) == [2, 2]

def test_counts_big_age_values_correctly():
    assert get_human_age(56, 0) == [8, 0]
    assert get_human_age(0, 73) == [0, 10]
    assert get_human_age(42, 90) == [5, 14]
    assert get_human_age(60, 30) == [9, 2]