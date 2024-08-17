from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0], \
        "For zero ages, [0, 0] should be returned"


def test_age_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0], \
        "If the age is less than 15 years, [0, 0] should be returned"


def test_age_equal_to_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1], \
        "At 15 years of age, [1, 1] should be returned"


def test_age_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1], \
        "At ages between 15 and 24 years, [1, 1] should be returned"
    assert get_human_age(24, 24) == [2, 2], \
        "At 24 years of age, [2, 2] should be returned"


def test_age_equal_to_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2], \
        "At 24 years of age, [2, 2] should be returned"


def test_age_above_second_threshold_but_below_next_cycle() -> None:
    assert get_human_age(27, 27) == [2, 2], \
        "At 27 years of age, [2, 2] should be returned"


def test_age_just_into_next_cycle() -> None:
    assert get_human_age(28, 28) == [3, 2], \
        "At 28 years of age, [3, 2] should be returned"


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17], \
        "At 100 years of age, [21, 17] should be returned"
