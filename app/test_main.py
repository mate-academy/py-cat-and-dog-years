from app.main import get_human_age

def test_human_age_for_zero_years():
    assert get_human_age(0, 0) == [0, 0]

def test_human_age_before_first_human_year():
    assert get_human_age(14, 14) == [0, 0]

def test_human_age_at_first_human_year():
    assert get_human_age(15, 15) == [1, 1]

def test_human_age_before_second_human_year():
    assert get_human_age(23, 23) == [1, 1]

def test_human_age_at_second_human_year():
    assert get_human_age(24, 24) == [2, 2]

def test_human_age_before_third_human_year():
    assert get_human_age(27, 27) == [2, 2]

def test_human_age_at_third_human_year():
    assert get_human_age(28, 28) == [3, 2]

def test_human_age_large_values():
    assert get_human_age(100, 100) == [21, 17]
