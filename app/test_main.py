from app.main import get_human_age


def test_should_return_zeros_if_age_of_animals_is_equal_to_0() -> None:
    assert get_human_age(0, 0) == [0, 0], "Result should be 0"


def test_should_return_zeros_if_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0], "Result should be 0"


def test_should_return_1_1_if_age_is_equal_to_15_15() -> None:
    assert get_human_age(15, 15) == [1, 1], "Result should be 1"


def test_should_return_1_1_if_age_is_equal_to_23_23() -> None:
    assert get_human_age(23, 23) == [1, 1], "Result should be 1"


def test_should_return_2_2_if_age_is_equal_to_24_24() -> None:
    assert get_human_age(24, 24) == [2, 2], "Result should be 2"


def test_should_return_2_2_if_age_is_equal_to_27_28() -> None:
    assert get_human_age(27, 28) == [2, 2], "Result should be 2"


def test_should_return_3_3_if_age_is_equal_to_28_29() -> None:
    assert get_human_age(28, 29) == [3, 3], "Result should be 3"


def test_should_return_21_17_if_age_is_equal_to_100_100() -> None:
    assert get_human_age(100, 100) == [21, 17], "Result should be 21, 17"
