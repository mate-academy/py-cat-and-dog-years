from app.main import get_human_age


def test_should_return_zero_when_ages_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_are_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_ages_are_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_are_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_for_27_cat_and_28_dog_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_three_for_28_cat_and_29_dog_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
