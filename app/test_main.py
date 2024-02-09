from app.main import get_human_age


def test_age_zero() -> None:
    assert get_human_age(0,0) == [0,0]


