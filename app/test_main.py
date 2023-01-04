from app.main import get_human_age

def test_when_input_is_zero() -> None:
    assert get_human_age(0,0) == [0, 0]

def test_when_input_is_negative() -> None:
    assert get_human_age(-11, -12) == [0, 0]

def test_must_be_0_if_input_is_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_should_be_1_if_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_must_be_1_if_input_is_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_should_convert_to_2_if_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_should_convert_to_2_if_age_less_then_28_and_29() -> None:
    assert get_human_age(27, 28) == [2, 2]

def test_should_convert_to_3_if_age_more_then_27_and_28() -> None:
    assert get_human_age(28, 29) == [3, 3]
