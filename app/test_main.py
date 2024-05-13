from app.main import get_human_age


def test_animal_not_first_year() -> None:
    assert get_human_age(14, 12) == [0, 0]


def test_animal_one_years() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_animal_two_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
