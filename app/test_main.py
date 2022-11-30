from app.main import get_human_age


def test_human_age_is_zero_if_animals_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_if_animal_age_is_less_than_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(12, 13) == [0, 0]


def test_if_animal_age_is_equal_to_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_animals_ages_equal_to_two_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 28) == [2, 2]


def test_animals_ages_equal_to_three_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_human_age_if_animals_age_more_than_three_human_years() -> None:
    assert get_human_age(32, 34) == [4, 4]
    assert get_human_age(100, 100) == [21, 17]
