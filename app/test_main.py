from app.main import get_human_age


def test_should_return_0_when_age_less_than_15() -> None:
    assert get_human_age(13, 13) == [0, 0]


def test_should_return_1_when_age_less_than_24() -> None:
    assert get_human_age(22, 23) == [1, 1]


def test_should_return_array_when_age_more_than_29() -> None:
    assert get_human_age(30, 46) == [3, 6]
