from app.main import get_human_age


def test_zero_when_age_less_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_more_than_15() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_more_24() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_age_dog_and_cat_should_be_different() -> None:
    assert get_human_age(100, 100) == [21, 17]
