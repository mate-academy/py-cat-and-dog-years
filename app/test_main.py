from app.main import get_human_age


def test_should_convert_to_0_if_age_less_then_15() -> None:
    goals = get_human_age(7, 7)
    assert goals == [0, 0]


def test_should_convert_to_1_if_age_15() -> None:
    goals = get_human_age(15, 15)
    assert goals == [1, 1]


def test_should_convert_to_1_if_age_less_then_24() -> None:
    goals = get_human_age(23, 23)
    assert goals == [1, 1]


def test_should_convert_to_2_if_age_24() -> None:
    goals = get_human_age(24, 24)
    assert goals == [2, 2]


def test_should_convert_to_if_age_less_then_28_and_29() -> None:
    goals = get_human_age(27, 28)
    assert goals == [2, 2]


def test_should_convert_to_3_or_more_if_age_more_then_27_and_28() -> None:
    goals = get_human_age(28, 29)
    assert goals == [3, 3]
