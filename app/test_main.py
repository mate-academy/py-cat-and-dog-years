from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_younger_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_still_be_one_between_15_and_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_still_be_two_for_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_diverge_after_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
