from app.main import get_human_age


def test_if_animal_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_if_animal_age_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animal_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_animal_age_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animal_age_have_second_human_age() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_animal_age_have_third_age() -> None:
    assert get_human_age(28, 29) == [3, 3]
