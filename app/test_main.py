from app.main import get_human_age


def test_should_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_convert_into_2_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_different_numbers() -> None:
    assert get_human_age(29, 28) == [3, 2]
