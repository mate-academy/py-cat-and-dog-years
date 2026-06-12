from app.main import get_human_age


def test_get_human_age_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_at_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_before_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_at_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_after_second_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_with_different_cat_and_dog_growth() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_with_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
