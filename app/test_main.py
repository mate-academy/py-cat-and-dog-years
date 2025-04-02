from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(1, 1) == [0, 0]


def test_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(16, 16) == [1, 1]


def test_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_after_second_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_different_conversion_rates() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_boundary_conditions() -> None:
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(31, 33) == [3, 3]
    assert get_human_age(32, 34) == [4, 4]
