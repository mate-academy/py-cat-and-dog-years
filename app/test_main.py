from app.main import get_human_age

# write your code here
def test_returns_zero_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_returns_zero_when_ages_are_fourteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_when_ages_are_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_returns_one_when_ages_are_twentythree() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_returns_two_when_ages_are_twentyfour() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_returns_two_when_ages_are_twentyseven() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_returns_three_for_cat_and_two_for_dog_when_ages_are_twenty_eight() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_returns_twentyone_for_dog_and_seventeen_for_cat_for_one_hundred_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
