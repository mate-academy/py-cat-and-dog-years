from app.main import get_human_age


def test_both_ages_zero_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_below_15_should_return_zero_human_years() -> None:
    assert get_human_age(14, 14) == [0, 0]



def test_ages_equal_to_15_should_return_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_ages_between_16_and_23_should_return_one_human_year_each() -> None:
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_ages_between_24_and_27_should_return_two_human_years_for_cat() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_ages_cat_28_dog_28_should_return_three_human_years_for_cat_two_for_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_ages_cat_100_dog_100_should_return_21_human_years_for_cat_17_for_dog() -> None:
    assert get_human_age(100, 100) == [21, 17]
