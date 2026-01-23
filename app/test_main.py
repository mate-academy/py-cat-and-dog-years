from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_less_than_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_human_year_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_not_increase_human_year_before_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_increase_human_year_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_handle_next_years_without_increment() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_calculate_cat_and_dog_years_differently() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_handle_large_ages_correctly() -> None:
    assert get_human_age(100, 100) == [21, 17]
