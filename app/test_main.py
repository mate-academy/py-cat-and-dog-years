from app.main import get_human_age

# write your code here
def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]

def test_under_15():
    assert get_human_age(14, 14) == [0, 0]

def test_exactly_15():
    assert get_human_age(15, 15) == [1, 1]

def test_under_24():
    assert get_human_age(23, 23) == [1, 1]

def test_exactly_24():
    assert get_human_age(24, 24) == [2, 2]

def test_under_28():
    assert get_human_age(27, 27) == [2, 2]

def test_exactly_28():
    assert get_human_age(28, 28) == [3, 2]

def test_large_numbers():
    assert get_human_age(100, 100) == [21, 17]
