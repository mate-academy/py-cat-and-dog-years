from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]

def test_age_below_15():
    assert get_human_age(14, 14) == [0, 0]

def test_age_exactly_15_years():
    assert get_human_age(15, 15) == [1, 1]

def test_age_between_15_and_23():
    assert get_human_age(23, 23) == [1, 1]

def test_age_exactly_24_years():
    assert get_human_age(24, 24) == [2, 2]

def test_age_between_24_years_and_next_step():
    assert get_human_age(25, 27) == [2, 2]

def test_exactly_28_years():
    assert get_human_age(28, 28) == [3, 2]

def test_high_age():
    assert get_human_age(100, 100) == [21, 17]

def test_cat_and_god_has_different_age():
    assert get_human_age(32, 20) == [4, 1]