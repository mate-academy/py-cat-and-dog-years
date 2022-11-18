from app.main import get_human_age


def test_negative_age_should_return_0_human_age() -> None:
    assert get_human_age(-15, -15) == [0, 0]


def test_0_age_should_return_0_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_1_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_between_1_and_2_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_more_than_2_years() -> None:
    assert get_human_age(24, 24) == [2, 2]
