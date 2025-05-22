from app.main import get_human_age

def test_if_pet_age_lower_15() -> None:
    human_age = get_human_age(14, 14)
    assert  human_age == [0, 0]


def test_if_pet_age_between_15_and_23() -> None:
    human_age = get_human_age(23, 23)
    assert  human_age == [1, 1]


def test_if_pet_age_27_28() -> None:
    human_age = get_human_age(27, 28)
    assert  human_age == [2, 2]


def test_if_animal_age_is_100() -> None:
    human_age = get_human_age(100, 100)
    assert human_age == [21, 17]
