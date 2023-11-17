from app.main import get_human_age


def test_should_return_0_if_animals_are_younger_than_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_if_animals_are_younger_than_24_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_correct_age_if_animals_older_than_24_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
