from app.main import get_human_age


def test_animals_does_not_have_a_year() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_animals_younger_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animals_younger_twenty_fours_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animals_before_twenty_eight_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_animals_after_twenty_eight_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_very_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
