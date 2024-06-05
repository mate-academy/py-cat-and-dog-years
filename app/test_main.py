from app.main import get_human_age


def test_should_return_zeros_when_inputs_are_zeros() -> None:
    expected_value = [0, 0]
    assert get_human_age(0, 0) == expected_value


def test_should_return_zeros_when_values_almost_15() -> None:
    expected_value = [0, 0]
    assert get_human_age(14, 14) == expected_value


def test_should_return_ones_when_values_are_exactly_15() -> None:
    expected_value = [1, 1]
    assert get_human_age(15, 15) == expected_value


def test_should_return_ones_when_values_are_almost_24() -> None:
    expected_value = [1, 1]
    assert get_human_age(23, 23) == expected_value


def test_should_return_twos_when_values_are_exactly_24() -> None:
    expected_value = [2, 2]
    assert get_human_age(24, 24) == expected_value


def test_should_return_twos_when_values_are_almost_27() -> None:
    expected_value = [2, 2]
    assert get_human_age(27, 27) == expected_value


def test_should_return_three_for_cat_and_two_for_dog_when_values_are_28() -> None:
    expected_value = [3, 2]
    assert get_human_age(28, 28) == expected_value


def test_should_return_two_plus_amount_of_animals_years_devided_by_5_for_cat_and_by_4_for_dog() -> None:
    expected_value = [21, 17]
    assert get_human_age(100, 100) == expected_value
