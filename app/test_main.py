from app.main import get_human_age

# write your code here
def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_before_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_average_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_old_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]

