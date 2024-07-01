from app.main import get_human_age


def test_should_return_zero_when_arguments_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_arguments_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_when_arguments_are_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_when_cat_year_less_than_28_end_dog_than_29() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_result_when_year_more_than_28_end_dog_than_29() -> None:
    assert get_human_age(100, 100) == [21, 17]
