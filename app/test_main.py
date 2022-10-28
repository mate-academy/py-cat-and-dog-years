from app.main import get_human_age

def test_should_return_one_when_input_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_zeros_when_input_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_input_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_when_input_equal_24() -> None:
    assert  get_human_age(24, 24) == [2, 2]


def test_should_return_expected_value_when_input_more_than_24() -> None:
    assert get_human_age(27, 28) == [2, 2]

def test_shoul_retern_expected_value_when_input_more_27() -> None:
    assert  get_human_age(28, 28) == [3, 2]

