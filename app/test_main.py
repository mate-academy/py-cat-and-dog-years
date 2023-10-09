from app.main import get_human_age


def test_animal_age_is_less_or_equal_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_animal_age_is_less_or_equal_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_animal_is_less_or_equal_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_animal_is_bigger_equal_27() -> None:
    assert get_human_age(28, 28) == [3, 2]
