from app.main import get_human_age


def test_if_inputs_values_are_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0], "False"


def test_inputs_smaller_then_default_values() -> None:
    assert get_human_age(14, 14) == [0, 0], "False"


def test_equals_values() -> None:
    assert get_human_age(15, 15) == [1, 1], "False"


def test_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17], "False"


def test_diffrent_ages() -> None:
    assert get_human_age(28, 30) == [3, 3], "False"


def test_diffrent_ages_cat_and_dog() -> None:
    assert get_human_age(23, 23) == [1, 1], "False"
