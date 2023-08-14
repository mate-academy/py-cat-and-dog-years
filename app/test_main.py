from app.main import get_human_age


def test_should_return_list_of_int() -> None:
    result = get_human_age(15, 15)
    assert (
        isinstance(result, list)
        and all(isinstance(element, int) for element in result)
    )


def test_get_human_age_should_return_zeros_for_zero_ages() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_get_human_age_should_return_zeros_if_less_than_15() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_get_human_age_should_check_if_more_than_14_less_than_24() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_get_human_age_should_check_if_more_than_23_less_than_28() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_get_human_age_should_check_difference_between_cat_dog_ages() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2]
