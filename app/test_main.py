from app.main import get_human_age


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_1_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
