from app.main import get_human_age


def test_both_ages_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_both_ages_under_15() -> None:
    assert get_human_age(10, 13) == [0, 0]


def test_both_ages_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_both_ages_between_15_and_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_both_ages_between_25_and_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_both_ages_over_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
