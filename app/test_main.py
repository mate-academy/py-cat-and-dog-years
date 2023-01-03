from app.main import get_human_age


def test_should_return_zero_human_age() -> None:
    goal = get_human_age(14, 14)
    assert goal == [0, 0]


def test_first_year_animal_life() -> None:
    goal = get_human_age(15, 15)
    assert goal == [1, 1]


def test_first_year_animal_life_ceil_value() -> None:
    goal = get_human_age(23, 23)
    assert goal == [1, 1]


def test_second_year_animal_life() -> None:
    goal = get_human_age(24, 24)
    assert goal == [2, 2]


def test_second_year_animal_life_ceil_value() -> None:
    goal = get_human_age(27, 27)
    assert goal == [2, 2]


def test_lasr_each_year_animal_life_for_cat() -> None:
    goal = get_human_age(28, 28)
    assert goal == [3, 2]


def test_lasr_each_year_animal_life_for_dog() -> None:
    goal = get_human_age(29, 29)
    assert goal == [3, 3]
