from app.main import get_human_age


def test_can_count_human_age_properly_when_both_ages_equal_14() -> None:
    assert (get_human_age(14, 14) == [0, 0])


def test_function_counts_human_age_properly_when_both_ages_equal_15() -> None:
    assert (get_human_age(15, 15) == [1, 1])


def test_function_counts_human_age_properly_when_both_ages_equal_24() -> None:
    assert (get_human_age(24, 24) == [2, 2])


def test_function_counts_human_age_properly_when_ages_are_different() -> None:
    assert (get_human_age(16, 83) == [1, 13])


def test_function_appends_zero_when_both_ages_are_negative() -> None:
    assert (get_human_age(-1, -1) == [0, 0])


def test_function_counts_properly_when_big_ages_are_given() -> None:
    assert (get_human_age(100, 100) == [21, 17])
