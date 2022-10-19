from app.main import get_human_age


def test_should_return_0_if_animal_age_less_then_15() -> None:
    assert get_human_age(12, 12) == [0, 0]


def test_should_return_1_if_animal_age_equal_to_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_1_if_animal_age_is_less_then_24() -> None:
    assert get_human_age(20, 20) == [1, 1]


def test_should_return_2_if_animal_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_2_if_animal_age_less_then_27cat_28dog() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_3_if_animal_age_equal_to_28cat_29dog() -> None:
    assert get_human_age(28, 29) == [3, 3]
