from app.main import get_human_age


def test_should_be_two_items_in_list() -> None:
    assert len(get_human_age(15, 15)) == 2, "get_human_age should return list with two items"


def test_return_same_age_if_cat_age_and_dog_age_less_than_15() -> None:
    assert get_human_age(10, 8) == [0, 0], "Age less than 15 should map to 0"


def test_return_age_of_1_when_cat_age_and_dog_age_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1], "Age equal to 15 should map to 1"


def test_return_age_of_1_when_cat_age_and_dog_age_between_15_and_24() -> None:
    result = get_human_age(20, 23)
    assert result == [1, 1], "Age between 15 and 24 should map to 1"


def test_return_age_of_2_when_cat_age_and_dog_age_equals_24() -> None:
    assert get_human_age(24, 24) == [2, 2], "Age equal to 24 should map to 2"


def test_cat_to_human_should_be_greater_if_both_value_equals_after_40() -> None:
    result = get_human_age(50, 50)
    assert result[0] > result[1], "Cat years should convert to greater human years after age 40"


def test_ages_should_convert_correctly_for_27_28_29_years() -> None:
    result_27_28 = get_human_age(27, 28)
    assert result_27_28 == [2, 2], "Cat age 27 and dog age 28 should both convert to 2 human years"

    result_28_29 = get_human_age(28, 29)
    assert result_28_29 == [3, 3], "Cat age 28 and dog age 29 should both convert to 3 human years"


def test_ages_edge_cases_28_29() -> None:
    assert get_human_age(28, 28) == [3, 2], "Cat and dog age 28 should convert to 3 human years"
    assert get_human_age(29, 29) == [3, 3], "Cat and dog age 29 should convert to 3 human years"