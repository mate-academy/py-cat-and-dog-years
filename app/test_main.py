from app.main import get_human_age


def test_get_human_age_lower_then_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_equal_to_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_equal_to_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_equal_to_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_equal_to_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
