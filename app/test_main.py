from app.main import get_human_age


def test_get_human_age_should_return_a_list_in_integers() -> None:
    result = get_human_age(28, 28)

    for age in result:
        assert isinstance(age, int)


def test_get_human_age_should_return_a_list_of_two_numbers() -> None:
    assert len(get_human_age(15, 15)) == 2


def test_get_human_age_if_cat_and_dog_years_less_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_if_cat_and_dog_years_less_24_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_if_cat_and_dog_years_equal_27_and_28_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_get_human_age_if_cat_and_dog_years_greater_27_and_28_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
