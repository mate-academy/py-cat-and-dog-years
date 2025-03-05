from app.main import get_human_age  # За потреби змініть шлях імпорту


def test_get_human_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exact_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_below_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_exact_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_just_below_next_increase() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_extra_dog_no_extra() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
