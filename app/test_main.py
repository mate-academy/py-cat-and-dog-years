from app.main import get_human_age


def test_should_return_zero_when_cat_and_dog_age_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_human_year_when_cat_and_dog_age_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_h_year_when_cat_and_dog_age_bw_15_and_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_human_years_when_cat_and_dog_age_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_correct_human_age_after_24_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_human_age_for_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_zero_when_cat_and_dog_age_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
