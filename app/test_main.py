from app.main import get_human_age


def test_zero_age_should_return_zero_human_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_year_should_return_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_first_year_should_return_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_less_than_second_threshold_should_return_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_threshold_should_return_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_threshold_should_still_return_two() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_one_extra_year_should_return_three() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age_should_return_expected_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_age_independent() -> None:
    assert get_human_age(100, 15) == [21, 1]
    assert get_human_age(15, 100) == [1, 17]
