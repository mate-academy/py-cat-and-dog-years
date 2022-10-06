from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_negative_ages() -> None:
    assert get_human_age(-1, -2) == [0, 0]


def test_age_lower_than_1_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_equals_to_1_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_between_1_and_2_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_equals_to_2_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_between_2_and_3_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_age_equals_to_3_years_for_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_equals_to_3_years_for_all_animals() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_age_more_then_10_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
