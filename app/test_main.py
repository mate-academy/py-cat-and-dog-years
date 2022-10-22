from app.main import get_human_age


def test_function_must_return_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_number_of_years_must_be_integer() -> None:
    func_result = get_human_age(25, 25)
    assert func_result == [int(func_result[0]), int(func_result[1])]


def test_cat_and_dog_min_years_life() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_max_cat_and_dog_years_to_0_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_min_cat_and_dog_years_to_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_max_cat_and_dog_years_to_1_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_min_cat_and_dog_years_to_2_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_max_cat_and_dog_years_to_2_human_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_years_more_than_2_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
