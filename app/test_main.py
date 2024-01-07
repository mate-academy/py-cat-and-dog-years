from app.main import get_human_age


def test_should_return_zero_years_for_first_14_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_right_years_for_first_animal() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_right_value() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_zero_years_for_zeros_years() -> None:
    assert get_human_age(0, 0) == [0, 0]

