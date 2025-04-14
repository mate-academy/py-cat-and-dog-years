from app.main import get_human_age


def test_age_below_14_should_be_equle_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_second_condtion_how_fast_getting_older() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_third_condition_how_fast_getting_older() -> None:
    assert get_human_age(28, 28) == [3, 2]
