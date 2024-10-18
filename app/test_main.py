from app.main import get_human_age


def cat_age_and_dog_age_eq() -> None:
    assert get_human_age(45, 45) == [7, 6]


def age_values_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def values_return_same_result() -> None:
    assert get_human_age(45, 49) == [7, 7]


def negative_values() -> None:
    assert get_human_age(-30, -28) == [0, 0]


def age_eq_to_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def checking_big_values() -> None:
    assert get_human_age(345453463, 435646354674) == [86363361, 87129270932]


def test_more_examples() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(23, 23) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]
    assert get_human_age(100, 100) == [21, 17]
