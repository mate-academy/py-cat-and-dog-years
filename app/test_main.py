from app.main import get_human_age


def test_should_return_zeros_if_cat_age_and_dog_age_less_than_15() -> None:
    result = get_human_age(cat_age=14, dog_age=14)
    assert (
        result == [0, 0]
    ), "Should return zeros if parameters less than 15"


def test_should_return_one_if_parameters_are_equal_to_15() -> None:
    result = get_human_age(cat_age=15, dog_age=15)
    assert (
        result == [1, 1]
    ), "Should return one if parameters equal 15"


def test_should_return_one_if_parameters_are_less_than_24() -> None:
    result = get_human_age(cat_age=23, dog_age=23)
    assert (
        result == [1, 1]
    ), "Should return one if parameters less than 24"


def test_should_return_two_if_parameters_are_more_than_24() -> None:
    result = get_human_age(cat_age=24, dog_age=24)
    assert (
        result == [2, 2]
    ), "Should return two if parameters more than 24"


def test_if_parameters_are_more_than_24_but_less_than_28() -> None:
    result = get_human_age(cat_age=26, dog_age=26)
    assert (
        result == [2, 2]
    ), "Should return two if parameters more than 24 and less than 28"


def test_if_parameters_are_equal_to_28() -> None:
    result = get_human_age(cat_age=28, dog_age=28)
    assert (
        result == [3, 2]
    ), "Should return [3, 2] if parameters equal 28"


def test_if_parameters_are_equal_to_100() -> None:
    result = get_human_age(cat_age=100, dog_age=100)
    assert (
        result == [21, 17]
    ), "Should return [21, 17] if parameters equal to 100"
