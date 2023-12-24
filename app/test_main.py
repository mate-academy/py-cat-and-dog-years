from app.main import get_human_age


def test_check_all_counted_parameters_cat_and_dog() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_if_zero_income() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_different_values_for_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_not_enough_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_one_year_age() -> None:
    assert get_human_age(15, 15) == [1, 1]
