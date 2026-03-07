from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_then_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_15_and_24_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_after_second_stage() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_next_stage_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
