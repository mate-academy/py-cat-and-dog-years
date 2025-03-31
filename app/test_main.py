from app.main import get_human_age

def test_get_human_age_zero_years():
    assert get_human_age(0, 0) == [0, 0], "Expected [0, 0] for cat and dog ages 0"

def test_get_human_age_less_then_first_threshold():
    assert get_human_age(14, 14) == [0, 0], "Expected [0, 0] for cat and dog ages 14"

def test_get_human_age_equal_first_threshold():
    assert get_human_age(15, 15) == [1, 1], "Expected [1, 1] for cat and dog ages 15"

def test_get_human_age_between_thresholds():
    assert get_human_age(23, 23) == [1, 1], "Expected [1, 1] for cat and dog ages 23"

def test_get_human_age_more_than_first_threshold():
    assert get_human_age(24, 24) == [2, 2], "Expected [2, 2] for cat and dog ages 24"

def test_get_human_age_between_more_than_first_threshold():
    assert get_human_age(27, 27) == [2, 2], "Expected [2, 2] for cat and dog ages 27"

def test_get_human_age_greater_than_threshold():
    assert get_human_age(28, 28) == [3, 2], "Expected [3, 2] for cat and dog ages 28"

def test_get_human_age_lage_ages():
    assert get_human_age(100, 100) ==[21, 17], "Expected [21, 17] for cat and dog ages"
