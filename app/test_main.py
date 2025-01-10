from app.main import get_human_age


def test_ages_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_animals_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_correct_age() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_animal_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_correct_age_after_two_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_three_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
