from app.main import get_human_age


def test_should_return_zero_when_pass_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_age_pass_negative() -> None:
    assert get_human_age(-10, 0) == [0, 0]
    assert get_human_age(1, -5) == [0, 0]


def test_should_cconvert_animal_years_less_than_human() -> None:
    assert get_human_age(14, 8) == [0, 0]


def test_should_convert_animal_years_to_human() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(15, 14) == [1, 0]


def test_should_convert_animal_years_equal_to_two_human() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_cat_years_equal_to_three_human() -> None:
    assert get_human_age(28, 25) == [3, 2]


def test_should_convert_dog_years_equal_to_three_human() -> None:
    assert get_human_age(27, 29) == [2, 3]
