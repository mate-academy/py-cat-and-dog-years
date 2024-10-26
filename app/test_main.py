from app.main import get_human_age


def test_human_age_if_animals_age_equal_zero() -> None:
    animals = get_human_age(0, 0)
    assert animals == [0, 0]


def test_human_age_if_animals_age_less_than_first_human_age() -> None:
    animals = get_human_age(7, 12)
    assert animals == [0, 0]


def test_human_age_if_animals_age_more_or_equal_than_first_human_age() -> None:
    animals = get_human_age(15, 17)
    assert animals == [1, 1]


def test_human_age_if_animals_age_more_or_equal_than_sum_first_and_second_human_age() -> None:
    animals = get_human_age(24, 24)
    assert animals == [2, 2]


def test_human_age_if_animals_age_more_or_equal_than_sum_first_and_second_and_each_human_age() -> None:
    animals = get_human_age(100, 100)
    assert animals == [21, 17]
