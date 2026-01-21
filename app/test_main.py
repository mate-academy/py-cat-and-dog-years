from app.main import get_human_age


def test_first_animal_years_up_to_15():
    assert get_human_age(14, 14) == [0, 0]


def test_first_15_animals_years():
    assert get_human_age(15, 15) == [1, 1]


def test_next_8_animals_years_after_15():
    assert get_human_age(23, 23) == [1, 1]


def test_next_9_animals_years_after_15():
    assert get_human_age(24, 24) == [2, 2]


def test_next_4_animals_years_after_9():
    assert get_human_age(27, 27) == [2, 2]


def test_next_5_animals_years_after_9():
    assert get_human_age(28, 28) == [3, 2]


def test_animals_years_with_all_conditions():
    assert get_human_age(100, 100) == [21, 17]
