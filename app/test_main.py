from app.main import get_human_age


def test_return_zero_until_animal_riches_15() -> None:
    assert get_human_age(14, 14) == [0, 0], \
        "Should return 0 if animal age less than 15 years"


def test_return_one_year_until_animal_riches_24() -> None:
    assert get_human_age(23, 23) == [1, 1], \
        "Should return 0 if animal age less than 15 years"


def test_returns_floored_values() -> None:
    assert get_human_age(33, 30) == [4, 3], \
        "Age should be a whole number of years"


def test_zero_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0], \
        "Should return 0 if animal age is 0"


def test_works_with_aged_animals() -> None:
    assert get_human_age(200, 200) == [46, 37], \
        "Should return correct values for aged animals"




