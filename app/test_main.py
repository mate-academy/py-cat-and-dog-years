from app.main import get_human_age


def test_should_check_if_years_more_than_15() -> None:
    assert (get_human_age(12, 12) == [0, 0])


def test_should_check_if_years_equivalent_15_and_should_add_1_human() -> None:
    assert (get_human_age(15, 15) == [1, 1])


def test_should_check_if_years_more_than_15_and_less_than_24() -> None:
    assert (get_human_age(23, 23) == [1, 1])


def test_should_check_if_years_equivalent_24() -> None:
    assert (get_human_age(24, 24) == [2, 2])


def test_should_check_if_years_more_than_24_and_less_than_28() -> None:
    assert (get_human_age(27, 27) == [2, 2])


def test_should_check_if_years_equivalent_28() -> None:
    assert (get_human_age(28, 28) == [3, 2])


def test_should_check_if_a_lot_of_cat_and_dogs_years_work_correctly() -> None:
    assert (get_human_age(100, 100) == [21, 17])
