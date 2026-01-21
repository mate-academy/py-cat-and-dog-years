from app.main import get_human_age


def test_should_return_0_human_years_when_animals_age_is_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_human_years_when_animals_age_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_human_years_when_animals_age_are_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_when_animals_age_between_15_and_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_human_years_when_animals_age_are_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_when_animals_years_are_27_28_cat_dog() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_0_when_animals_year_lower_0() -> None:
    assert get_human_age(-98, -98) == [0, 0]


def test_should_return_integer_human_years_for_cat_years() -> None:
    assert isinstance(get_human_age(50, 50)[0], int)


def test_should_return_integer_human_years_for_dog_years() -> None:
    assert isinstance(get_human_age(50, 50)[1], int)
