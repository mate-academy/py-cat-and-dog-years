from app.main import get_human_age

def test_get_human_age_zero_ages():
    assert get_human_age(0, 0) == [0, 0]

def test_get_human_age_below_first_threshold():
    assert get_human_age(14, 14) == [0, 0]

def test_get_human_age_at_first_threshold():
    assert get_human_age(15, 15) == [1, 1]

def test_get_human_age_within_second_threshold():
    assert get_human_age(23, 23) == [1, 1]

def test_get_human_age_at_second_threshold():
    assert get_human_age(24, 24) == [2, 2]

def test_get_human_age_below_next_increment():
    assert get_human_age(27, 27) == [2, 2]

def test_get_human_age_start_next_increment():
    assert get_human_age(28, 28) == [3, 2]

def test_get_human_age_large_ages():
    assert get_human_age(100, 100) == [21, 17]

def test_get_human_age_mixed_values():
    assert get_human_age(20, 50) == [1, 7]
    assert get_human_age(30, 10) == [3, 0]
    assert get_human_age(45, 65) == [7, 10]
