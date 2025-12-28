from app.main import get_human_age


def test_should_return_zero_if_boundary_values_is_zero() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "should return zero if boundary values is zero 0, 0 == [0, 0]"


def test_should_return_zero_if_no_full_fifteen_years() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "should return zero if no full fifteen years 14, 14 == [0, 0]"


def test_should_return_one_if_pet_has_full_fifteen_years() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "should return one if pet has full full fifteen years 15, 15 == [0, 0]"


def test_should_return_one_because_we_take_whole_number_of_years() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), ("should return one because we take"
        " whole number of years 23, 23 == [1, 1]")


def test_check_calculation_difference_between_cat_and_dog_years() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    ), ("Check calculation difference between "
        "cat and dog years 28, 28 == [3, 2]")
