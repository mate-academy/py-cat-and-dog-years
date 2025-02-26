from app.main import get_human_age


def test_should_return_zero_for_age_below_15() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]

def test_should_return_one_for_age_between_15_and_23() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]

def test_should_return_two_for_age_between_24_and_27() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]

def test_should_return_different_ages_for_28_years():
    assert get_human_age(28, 28) == [3, 2]

def test_should_return_correct_age_for_large_values():
    assert get_human_age(100, 100) == [21, 17]
