from app.main import get_human_age


def test_human_age_shouldbe_zero_if_animals_are_under_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_human_age_shouldbe_one_if_animals_are_under_twenty_four() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_be_the_same_for_different_years() -> None:
    assert get_human_age(44, 44) == [7, 6]
