from app.main import get_human_age


def test_the_animal_is_one_year_old() -> None:
    assert get_human_age(23, 15) == [1, 1]


def test_the_animal_is_two_year_old() -> None:
    assert get_human_age(24, 27) == [2, 2]


def test_each_subsequent_year() -> None:
    assert get_human_age(28, 29) == [3, 3]
