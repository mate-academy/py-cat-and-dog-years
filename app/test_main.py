from app.main import get_human_age


def test_age_zero_equals_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_lower_than_first_year_equals_zero() -> None:
    assert get_human_age(14, 13) == [0, 0]


def test_age_first_year_equals_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_23_should_return_2_for_both() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_24_should_return_2_for_both() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_equals_2_human_for_both() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_age_equals_3_human_for_both() -> None:
    assert get_human_age(28, 28) == [3, 2]
