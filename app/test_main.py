from app.main import get_human_age


def test_when_age_is_zero_should_return_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_when_age_less_than_first_year_should_return_zeros() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_when_age_less_than_second_year_should_return_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_each_year_after_two_human() -> None:
    assert get_human_age(100, 100) == [21, 17]
