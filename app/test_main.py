from app.main import get_human_age


def test_elements_should_be_equal_to_result() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_result_should_return_zeros_if_years_equal_to_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_rounded_down_result() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_count_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_different_values_for_the_same_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
