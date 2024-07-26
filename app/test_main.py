from app.main import get_human_age


def test_should_return_zero_when_input_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_age_is_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_correct_result_after_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_correct_result_between_15_and_next_9_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_correct_result_after_9_more_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_correct_result_between_9_and_next_4_cat_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_correct_cat_next_4_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_dog_next_5_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_result_over_a_long_period_of_time() -> None:
    assert get_human_age(100, 100) == [21, 17]
