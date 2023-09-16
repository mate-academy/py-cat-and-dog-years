from app.main import get_human_age


def test_check_output_value_not_equal_previous_value() -> None:
    assert (get_human_age(cat_age=23, dog_age=23)
            != get_human_age(cat_age=24, dog_age=24))


def test_check_resive_data_minus_value_or_zero_value() -> None:
    assert get_human_age(cat_age=0, dog_age=-16) == [0, 0]


def test_check_get_human_age_return_list() -> None:
    assert isinstance(get_human_age(cat_age=10, dog_age=10), list)


def test_check_age_if_cat_dog_age_equal_tw_eight() -> None:
    assert get_human_age(cat_age=28, dog_age=28) == [3, 2]


def test_check_correct_type_of_value() -> None:
    data_type = get_human_age(cat_age=10, dog_age=10)
    assert isinstance(data_type[0], int)
    assert isinstance(data_type[1], int)
