from app.main import get_human_age


def test_should_return_zero_if_years_less_than_16() -> None:
    assert get_human_age(10, 13) == [0, 0]


def test_should_return_1_if_years_less_than_24() -> None:
    assert get_human_age(20, 23) == [1, 1]


def test_should_return_correct_count_if_years_more_than_23() -> None:
    assert get_human_age(48, 54) == [8, 8]


def test_should_return_correct_count_many_years_rounding() -> None:
    assert get_human_age(50, 56) == [8, 8]


def test_should_separate_count_for_dog_cat_years() -> None:
    assert get_human_age(50, 12) == [8, 0]
