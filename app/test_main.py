from app.main import get_human_age


def test_should_return_0_when_age_less_than_15() -> None:
    assert get_human_age(15, 14) == [1, 0]


def test_should_return_1_when_age_less_than_24() -> None:
    assert get_human_age(24, 23) == [2, 1]


def test_should_return_array_when_age_bigger_29() -> None:
    assert get_human_age(27, 29) == [2, 3]
