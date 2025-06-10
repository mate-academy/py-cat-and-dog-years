from app.main import get_human_age


def test_dog_zero_and_cat_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_condition() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_second_condition() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_third_condition() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_fourth_condition() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_fifth_condition() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_sixth_condition() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_seventh_condition() -> None:
    assert get_human_age(100, 100) == [21, 17]
