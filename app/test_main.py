from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_two_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_when_one_animal_is_older_another_in_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_three_human_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_many_years_animal() -> None:
    assert get_human_age(100, 100) == [21, 17]
