from app.main import get_human_age

def test_get_human_age_should_return_animal_age_in_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_with_negative_numbers() -> None:
    assert get_human_age(-19, -74) == [0, 0]


def test_get_human_age_with_big_numbers() -> None:
    assert get_human_age(1000, 789) == [246, 155]