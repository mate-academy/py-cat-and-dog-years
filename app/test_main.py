from app.main import get_human_age


def test_when_pets_ages_less_than_1_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_when_pet_ages_are_exactly_1_huma_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_when_pets_ages_greater_than_1_human_year() -> None:
    assert get_human_age(22, 22) == [1, 1]


def test_when_pets_ages_are_exactly_2_human_year() -> None:
    assert get_human_age(25, 25) == [2, 2]


def test_when_dog_human_age_is_lower_than_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_when_pet_ages_are_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
