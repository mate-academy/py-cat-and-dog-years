from app.main import get_human_age


def test_should_return_zero_for_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_for_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_for_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_for_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_for_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_and_two_for_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_twenty_one_and_seventeen_for_100() -> None:
    assert get_human_age(28, 28) == [21, 17]
