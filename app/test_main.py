from app.main import get_human_age


def test_animal_age_is_lower_than_1_human_years() -> None:
    assert (get_human_age(14, 14) == [0, 0])


def test_animal_age_between_1_and_2_human_years() -> None:
    assert (get_human_age(23, 23) == [1, 1])


def test_animal_age_between_2_and_3_human_years() -> None:
    assert (get_human_age(27, 28) == [2, 2])


def test_animal_age_above_3_human_years() -> None:
    assert (get_human_age(28, 29) == [3, 3])
