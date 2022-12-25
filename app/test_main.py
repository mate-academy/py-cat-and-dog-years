from app.main import get_human_age


def test_should_be_add_zero_when_age_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_convert_age_into_human_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_convert_age_into_one_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1]
