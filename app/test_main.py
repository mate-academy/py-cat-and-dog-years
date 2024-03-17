from app.main import get_human_age


def test_both_animal_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_the_first_animal_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_is_exactly_one_animal_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_less_the_second_animal_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_is_exactly_two_animal_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_less_third_first_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_is_exactly_tree_animal_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
