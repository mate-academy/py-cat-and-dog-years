from app.main import get_human_age


def test_result_should_zeroes_when_given_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeroes_if_less_then_one_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_if_between_one_and_two_humans_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_equals_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_different_humans_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_result_for_age_more_than_three() -> None:
    assert get_human_age(62, 74) == [11, 12]
