from app.main import get_human_age


def test_result_list_should_contain_two_values() -> None:
    assert len(get_human_age(18, 14)) == 2


def test_should_return_zeroes_when_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_age_less_then_15() -> None:
    assert get_human_age(12, 14) == [0, 0]


def test_should_return_one_when_age_equals_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_when_age_equals_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_three_and_two_when_age_equals_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_three_when_age_equals_29() -> None:
    assert get_human_age(29, 29) == [3, 3]
