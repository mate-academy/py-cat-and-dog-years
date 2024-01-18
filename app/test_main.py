from app.main import get_human_age


def test_should_return_zero_years_if_less_than_15() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Should return zero cat/dog years if human age less than 15"


def test_should_return_one_years_if_more_than_15() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Should return 1 cat/dog years if human age more than 15"


def test_should_return_one_years_if_less_than_24() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "Should return 1 cat/dog years if human age less than 23"


def test_should_return_one_years_if_more_than_24() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "Should return 2 cat/dog years if human age more than 24"


def test_should_return_two_years_if_more_than_27_cat_28_dog() -> None:
    assert (
        get_human_age(27, 28) == [2, 2]
    ), ("Should return 2 cat/dog years if human age for cat is "
        "27 and 28 for dog")


def test_should_return_three_years_if_more_than_28_cat_29_dog() -> None:
    assert (
        get_human_age(28, 29) == [3, 3]
    ), ("Should return 3 cat/dog years if human age for cat is "
        "28 and 29 for dog")
