from app.main import get_human_age


def test_should_add_zeros_when_age_less_then_15() -> None:
    goals = get_human_age(14, 14)
    assert goals == [0, 0]


def test_should_add_units_when_age_between_15_and_23() -> None:
    goals = get_human_age(15, 23)
    assert goals == [1, 1]


def test_should_add_deuces_when_age_less_then_28() -> None:
    goals = get_human_age(27, 27)
    assert goals == [2, 2]


def test_when_age_more_then_28() -> None:
    goals = get_human_age(28, 28)
    assert goals == [3, 2]


def test_when_age_100() -> None:
    goals = get_human_age(100, 100)
    assert goals == [21, 17]
