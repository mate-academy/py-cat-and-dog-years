from app.main import get_human_age


def test_animal_age_is_lower_than_first_year() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_animal_age_between_first_and_second_year() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_animal_age_is_equal_to_first_year_and_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_animal_age_is_between_second_year_and_each_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_animal_age_is_greater_than_first_year_and_second_each_year() -> None:
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(100, 100) == [21, 17]
