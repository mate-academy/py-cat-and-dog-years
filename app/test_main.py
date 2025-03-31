from app.main import get_human_age


def test_animal_first_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animal_second_age() -> None:
    assert get_human_age(23, 15) == [1, 1]


def test_animal_third_age() -> None:
    assert get_human_age(40, 40) == [6, 5]


def test_animal_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
