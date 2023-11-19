from app.main import get_human_age


def test_both_ages_zero_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_below_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_ages_equal_to_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_between_16_and_23() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_ages_between_24_and_27() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_ages_cat_28_dog_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_ages_cat_100_dog_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
