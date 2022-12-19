from app.main import get_human_age


def test_should_convert_into_1_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_convert_into_2_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]
