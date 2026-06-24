import app.main as main


def test_get_human_age_zero() -> None:
    assert main.get_human_age(0, 0) == [0, 0]


def test_get_human_age_below_first_threshold() -> None:
    assert main.get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_year() -> None:
    assert main.get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_first_and_second() -> None:
    assert main.get_human_age(23, 23) == [1, 1]


def test_get_human_age_second_year_boundary() -> None:
    assert main.get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_different_growth_rules() -> None:
    assert main.get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert main.get_human_age(100, 100) == [21, 17]


def test_cat_and_dog_different_inputs() -> None:
    assert main.get_human_age(28, 32) == [3, 3]
