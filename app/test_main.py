from app.main import get_human_age


def test_control_age_should_be_0() -> None:
    old = get_human_age(14, 14)
    assert old == [0, 0]


def test_should_be_more_0() -> None:
    old = get_human_age(15, 15)
    assert old == [1, 1]


def test_control_should_be_2() -> None:
    old = get_human_age(24, 24)
    assert old == [2, 2]


def test_control_age() -> None:
    old = get_human_age(28, 28)
    assert old == [3, 2]
