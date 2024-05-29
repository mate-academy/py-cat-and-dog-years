from app.main import get_human_age


def test_should_return_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_animals_have_not_a_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_animals_have_one_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_animals_have_two_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_animal_have_different_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_animals_have_their_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
