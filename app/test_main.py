from app.main import get_human_age


def test_returns_zero_for_age_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_for_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_zero_when_both_ages_are_less_than_15() -> None:
    assert get_human_age(10, 10) == [0, 0]


def test_should_return_one_when_ages_are_between_15_and_23() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(20, 20) == [1, 1]


def test_should_return_two_when_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_calculate_additional_cat_years_correctly() -> None:
    assert get_human_age(28, 24) == [3, 2]


def test_should_calculate_additional_dog_years_correctly() -> None:
    assert get_human_age(24, 29) == [2, 3]


def test_should_handle_mixed_values_correctly() -> None:
    assert get_human_age(32, 39) == [4, 5]


def test_should_floor_values() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_handle_large_values() -> None:
    assert get_human_age(100, 100) == [
        2 + (100 - 24) // 4,
        2 + (100 - 24) // 5,
    ]
