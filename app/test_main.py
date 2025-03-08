from app.main import get_human_age


def test_zero_age_for_pets() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_first_element_zero_if_cat_is_young() -> None:
    assert get_human_age(14, 17) == [0, 1]


def test_second_element_zero_if_dog_is_young() -> None:
    assert get_human_age(17, 14) == [1, 0]


def test_first_element_one_if_cat_is_middle_age() -> None:
    assert get_human_age(23, 32) == [1, 3]


def test_second_element_one_if_dog_is_middle_age() -> None:
    assert get_human_age(35, 22) == [4, 1]


def test_first_element_correct_if_cat_is_old() -> None:
    assert get_human_age(54, 19) == [9, 1]


def test_second_element_correct_if_dog_is_old() -> None:
    assert get_human_age(32, 100) == [4, 17]


def test_diff_values_if_age_is_equal_and_above_27() -> None:
    assert get_human_age(28, 28) == [3, 2]
