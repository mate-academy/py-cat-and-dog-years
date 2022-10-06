from app.main import get_human_age


def test_should_return_0_when_age_is_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_when_age_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_age_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_when_age_greater_23() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_if_cat_age_is_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_if_dog_age_is_29() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_age_more_then_29() -> None:
    assert get_human_age(100, 100) == [21, 17]
