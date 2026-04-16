from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_equals_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_in_second_period() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_differ_in_third_period() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
