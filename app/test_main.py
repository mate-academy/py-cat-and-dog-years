from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]


def test_second_9_years() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_rest_of_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
