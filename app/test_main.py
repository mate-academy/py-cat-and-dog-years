from app.main import get_human_age


def test_should_convert_less_than_15_years_to_zero() -> None:

    assert get_human_age(14, 14) == [0, 0]


def test_should_convert_next_9_years_to_1() -> None:

    assert get_human_age(23, 23) == [1, 1]


def test_should_return_same_value_up_to_28_years_old() -> None:
    assert get_human_age(27, 27)[0] == get_human_age(27, 27)[1]


def test_should_return_different_value_after_next_4_years() -> None:

    assert get_human_age(28, 28)[0] != get_human_age(28, 28)[1]
