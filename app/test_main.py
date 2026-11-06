import app.main
from app.main import get_human_age


def test_should_return_zeros_if_ages_are_zero() -> None:
    assert get_human_age  # Щоб flake8 не видавав помилку F401
    assert app.main.get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_if_ages_are_less_than_15() -> None:
    assert app.main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_if_ages_are_exactly_15() -> None:
    assert app.main.get_human_age(15, 15) == [1, 1]


def test_should_return_one_if_ages_are_between_15_and_24() -> None:
    assert app.main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_if_ages_are_exactly_24() -> None:
    assert app.main.get_human_age(24, 24) == [2, 2]


def test_should_calculate_correctly_for_ages_more_than_24() -> None:
    assert app.main.get_human_age(27, 27) == [2, 2]
    assert app.main.get_human_age(28, 28) == [3, 2]
    assert app.main.get_human_age(28, 29) == [3, 3]
    assert app.main.get_human_age(100, 100) == [21, 17]


def test_should_handle_different_ages_for_cat_and_dog() -> None:
    assert app.main.get_human_age(14, 28) == [0, 2]
    assert app.main.get_human_age(28, 14) == [3, 0]
