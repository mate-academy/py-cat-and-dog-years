from app import main


def test_should_return_zero_when_age_is_zero() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_should_return_zero_before_first_threshold() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_should_return_one_at_first_threshold() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_should_return_one_before_second_threshold() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_second_threshold() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_should_return_two_before_third_increment() -> None:
    assert main.get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_should_diverge_after_second_threshold() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_should_calculate_large_ages_correctly() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_should_discard_remainder_in_intermediate_steps() -> None:
    result = main.get_human_age(1, 1)
    assert result == [0, 0]
