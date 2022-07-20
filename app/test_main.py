from app.main import get_human_age


def test_first_animal_years_up_to_15():
    assert get_human_age(7, 7) == [0, 0]


def test_first_15_animals_years():
    assert get_human_age(15, 15) == [1, 1]


def test_next_animals_years_after_15():
    assert get_human_age(100, 100) == [21, 17]
