from app.main import get_human_age


def test_if_years_equals_to_zero() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_pet_years_not_enough_for_human_years() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_years_equals_to_1_without_rest() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_years_greater_than_1_human_but_lower_than_2() -> None:
    result = get_human_age(23, 23)
    assert result == [1, 1]


def test_pet_years_equals_to_2_human_years_without_rest() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_pet_years_not_enough_for_3_human_years() -> None:
    result = get_human_age(27, 27)
    assert result == [2, 2]


def cat_years_should_convert_into_3_human_age() -> None:
    result = get_human_age(28, 29)
    assert result == [3, 3]


def pet_years_equals_to_100() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]
