from app.main import get_human_age


def test_convert_age_to_human_years_when_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_convert_age_to_human_years_when_age_from_15_to_24() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_convert_to_human_years_when_age_more_than_24() -> None:
    assert get_human_age(28, 28) == [3, 2]
