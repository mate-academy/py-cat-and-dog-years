from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_below_15_years() -> None:
    assert get_human_age(14, 0) == [0, 0]


def test_cat_first_15_years() -> None:
    assert get_human_age(15, 0) == [1, 0]


def test_cat_next_9_years() -> None:
    assert get_human_age(24, 0) == [2, 0]


def test_cat_next_4_years() -> None:
    assert get_human_age(28, 0) == [3, 0]


def test_dog_below_15_years() -> None:
    assert get_human_age(0, 14) == [0, 0]


def test_dog_first_15_years() -> None:
    assert get_human_age(0, 15) == [0, 1]


def test_dog_next_9_years() -> None:
    assert get_human_age(0, 24) == [0, 2]


def test_dog_next_5_years() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_mixed_ages() -> None:
    assert get_human_age(20, 30) == [1, 3]


def test_23_years_dog() -> None:
    assert get_human_age(0, 23) == [0, 1]
