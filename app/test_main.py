from app.main import get_human_age


def test_get_human_age_convert_to_four() -> None:
    assert get_human_age(32, 34) == [4, 4]


def test_get_human_age_convert_different() -> None:
    assert get_human_age(14, 28) == [0, 2]
