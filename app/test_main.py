from app.main import get_human_age


def test_returns_zero_for_ages_less_than_15() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_returns_one_for_ages_between_15_and_23()-> None:
    assert get_human_age(15, 15) == [1, 1]


def test_returns_two_for_ages_between_24_and_27() -> None:
    assert get_human_age(24, 27) == [2, 2]


def test_returns_two_for_ages_between_28_and_31()-> None:
    assert get_human_age(28, 31) == [3, 3]

def test_returns_different_values_for_cat_and_dog()-> None:
    assert get_human_age(28, 28) == [3, 2]


def test_returns_three_for_large_ages()-> None:
    assert get_human_age(100, 100) == [21, 17]
