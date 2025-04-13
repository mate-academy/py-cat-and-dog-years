from app.main import get_human_age

def test_if_cat_and_dog_age_are_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_for_zero_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_for_one_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_for_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_for_three_human_years() -> None:
    assert get_human_age(28, 29) == [3, 3]

def test_with_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
