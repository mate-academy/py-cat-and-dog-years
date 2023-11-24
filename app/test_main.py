from app.main import get_human_age


def test_initial_conditions() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_before_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_third_threshold() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_larger_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
