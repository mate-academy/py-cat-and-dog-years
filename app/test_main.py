from app.main import get_human_age


def test_if_animals_years_are_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_specific_animal_ages() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(100, 100) == [21, 17]
