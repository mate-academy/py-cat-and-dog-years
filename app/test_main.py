from app.main import get_human_age


def test_should_return_zero_when_age_less_then_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_year_when_age_less_then_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_years_when_age_equal_27_for_cat_28_for_dog() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_three_years_when_age_equal_28_for_cat_29_for_dog() -> None:
    assert get_human_age(28, 29) == [3, 3]
