from app.main import get_human_age


def test_should_return_zeros_if_cat_and_dog_age_is_zero() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "Function should return zeros if cat/dog age is zero"


def test_should_return_one_year_if_cat_and_dog_age_is_15() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Function should return one year if cat/dog age is 15"


def test_should_return_different_age_with_same_input_ages() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "Function should return different cat/dog age on age of 28"


def test_should_return_same_age_with_different_input_ages() -> None:
    assert (
        get_human_age(28, 29) == [3, 3]
    ), "Function should return same cat/dog age on age of 29/28"


def test_should_return_age_of_the_most_old_cat_and_dog() -> None:
    assert (
        get_human_age(168, 164) == [38, 30]
    ), "Function should return age of the oldest cat/dog in the world (38/30)"
