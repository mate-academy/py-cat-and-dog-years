from app.main import get_human_age


def test_should_convert_to_0_if_age_less_then_15() -> None:
    assert get_human_age(7, 7) == [0, 0]


def test_should_convert_to_1_if_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_convert_to_1_if_age_less_then_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_convert_to_2_if_age_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_to_if_age_less_then_28_and_29() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_convert_to_3_or_more_if_age_more_then_27_and_28() -> None:
    assert get_human_age(28, 29) == [3, 3]


