from app.main import get_human_age


def test_should_return_0_0_for_0_0_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_0_0_for_14_14_ages() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_1_for_15_15_ages() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_1_for_23_23_ages() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_2_for_24_24_ages() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_2_for_27_27_ages() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_3_2_for_28_28_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_17_for_100_100_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
