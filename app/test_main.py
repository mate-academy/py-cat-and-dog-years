from app.main import get_human_age


def test_func_if_zeroes_given() -> None:
    goals = get_human_age(0, 0)
    assert goals == [0, 0]


def test_if_ages_less_than_first_animal_year() -> None:
    goals = get_human_age(14, 14)
    assert goals == [0, 0]


def test_if_ages_same_as_first_animal_year() -> None:
    goals = get_human_age(15, 15)
    assert goals == [1, 1]


def test_if_ages_less_than_second_animal_year() -> None:
    goals = get_human_age(23, 23)
    assert goals == [1, 1]


def test_if_ages_exact_second_animal_year() -> None:
    goals = get_human_age(24, 24)
    assert goals == [2, 2]


def test_if_ages_exact_third_animal_year() -> None:
    goals = get_human_age(28, 28)
    assert goals == [3, 2]
