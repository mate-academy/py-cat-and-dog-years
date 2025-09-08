from app.main import get_human_age


def test_returns_zero_on_zero_years() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "Should return zero if age of animal is zero"


def test_returns_zero_if_less_than_15() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Should return zero if age of animal is less than 15"


def test_returns_one_if_age_is_15() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Should return 1 if age of animal equals 15"


def test_returns_one_if_age_is_between_15_and_24() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "Should return 1 if age of animal less than 15 + 9, but more than 15"


def test_result_for_both_is_2_if_age_less_than_28() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "If age less than 24, for both  human age must be 2"


def test_on_age_equals_28_cats_start_aging_and_dogs_dont() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "If age is 28, cats start to age, changing to 3 and dogs stay at 2"


def test_difference_in_cat_and_dog_age_for_greater_numbers() -> None:
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "Difference between cats and dogs age is increasing on greater numbers"
