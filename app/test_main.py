from app.main import get_human_age


def test_get_human_age_should_be_equal_to_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_should_be_equal_to_one() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_should_be_equal_to_two() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]


def test_get_human_age_should_be_equal_to_more_then_two() -> None:
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(100, 100) == [21, 17]
