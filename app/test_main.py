from app.main import get_human_age

def test_should_return_zero_if_age_is_under_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_one_if_age_is_over_fifteen_and_under_twenty_four() -> None:
    assert get_human_age(15, 23) == [1, 1]

def test_should_return_correct_age_of_four() -> None:
    assert get_human_age(32, 34) == [4, 4]

def test_should_return_different_age() -> None:
    assert get_human_age(28, 28) == [3, 2]
