from app.main import get_human_age


def test_returns_zero_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_at_first_conversion_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_returns_one_before_second_conversion_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_returns_two_at_second_conversion_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_have_different_extra_year_steps() -> None:
    assert get_human_age(28, 28) == [3, 2]
