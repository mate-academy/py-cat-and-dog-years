from app.main import get_human_age


def test_age_cant_be_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_of_animals_less_15() -> None:
    assert get_human_age(12, 14) == [0, 0]


def test_animals_15_years_old() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_animals_23_years_old() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animals_24_years_old() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_animals_27_years_old() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_animals_28_years_old() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_animals_100_years_old() -> None:
    assert get_human_age(100, 100) == [21, 17]
