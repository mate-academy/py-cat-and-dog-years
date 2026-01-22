from app.main import get_human_age


def test_zero_ages_should_return_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_ages_just_below_first_year_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_ages_equal_to_first_year_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_below_second_year_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_ages_equal_to_second_year_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_ages_just_below_next_conversion_step() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_age_goes_up_before_dog_due_to_smaller_step() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_with_different_ages() -> None:
    assert get_human_age(50, 20) == [
        2 + (50 - 15 - 9) // 4,
        1
    ]


def test_boundary_conditions_cat_and_dog() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(29, 29) == [3, 3]
