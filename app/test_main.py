from app.main import get_human_age


def test_should_return_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_default_return() -> None:
    assert get_human_age(21, 15) == [1, 1]


def test_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2]
