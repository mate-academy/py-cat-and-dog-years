from app.main import get_human_age


def test_should_return_zero_for_both() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_both() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_end_of_first_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_for_both() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_for_both_end_of_second_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_three_for_both() -> None:
    assert get_human_age(28, 29) == [3, 3]
