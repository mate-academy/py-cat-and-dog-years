from app.main import get_human_age


def test_should_return_zero_human_years_when_animal_years_less_than_15(
) -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_human_years_when_animal_years_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_2_human_years_when_animal_years_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_calculate_human_years_when_animal_years_more_than_24() -> None:
    assert get_human_age(36, 34) == [5, 4]
