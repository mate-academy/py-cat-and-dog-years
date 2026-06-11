from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(25, 25) == [3, 3]
    assert get_human_age(28, 30) == [4, 4]
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_with_different_values() -> None:
    assert get_human_age(15, 7) == [1, 0]
    assert get_human_age(17, 23) == [1, 1]


def test_get_human_age_when_value_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
